# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
方法一：暴力法
空间复杂度(1)，时间复杂度O(mn)，m和n为两个链表长度
'''


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        node1 = headA
        while node1:
            node2 = headB
            while node2:
                if node2 is node1:
                    return node2
                node2 = node2.next
            node1 = node1.next
        return None


'''
方法二：使用哈希表存储
空间复杂度(m)，时间复杂度O(m+n)，m和n为两个链表长度
'''


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        node = headA
        dic = {}
        while node:
            dic[node] = 1
            node = node.next
        node = headB
        while node:
            if dic.get(node):
                return node
            node = node.next
        return None


'''
方法三：使用双指针，一个指针走到当前；列表末尾后移到另一个链表头
空间复杂度(1)，时间复杂度O(m+n)，m和n为两个链表长度
'''


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        node1, node2 = headA, headB
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        return node1
