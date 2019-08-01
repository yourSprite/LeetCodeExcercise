'''
空间复杂度O(1)，时间复杂度O(n)
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        pre, node = head, head
        while node:
            if node.val == val:
                pre.next = node.next
                node = node.next
            else:
                pre, node = node, node.next
        return head
