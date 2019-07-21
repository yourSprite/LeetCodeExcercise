# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
方法一：哈希表
空间复杂度O(n)，时间复杂度O(n)
'''


class Solution(object):
    def hasCycle(self, head):
        dic = {}
        node = head
        while node:
            if dic.get(node.next):
                return True
            else:
                dic[node.next] = 1
            node = node.next
        return False


'''
方法二：快慢指针
空间复杂度O(1)，时间复杂度O(n)
'''


class Solution(object):
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False


'''
方法三：空置法，在原链表上直接操作
空间复杂度O(1)，时间复杂度O(n)
'''


class Solution(object):
    def hasCycle(self, head):
        node = head
        while node:
            if not node.val:
                return True
            else:
                node.val = None
            node = node.next
        return False
