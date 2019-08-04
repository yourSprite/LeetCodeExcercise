# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
方法一：使用列表存储链表
空间复杂度O(n)，时间复杂度O(n)
'''


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l[::] == l[::-1]


''''
方法二：快慢指针+反转链表
空间复杂度O(1)，时间复杂度O(n)
'''


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow, fast = head, head
        prev = None
        # 遍历前半段并反转链表
        while fast.next and fast.next.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
            temp.next, prev = prev, temp
        # 判断链表长度奇偶
        if fast.next:  # 偶数，注意这里slow是没有反转的
            p1 = slow
            p2 = slow.next
            slow.next = prev
        else:  # 奇数
            p1 = prev
            p2 = slow.next
        while p1:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
