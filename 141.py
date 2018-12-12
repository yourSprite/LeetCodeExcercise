# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head# 初始化快慢指针
        while fast and fast.next:# 初始节点不为空并且下一个节点不为空
            fast = fast.next.next# 快指针每次走两步
            slow = slow.next# 慢指针每次走一步
            if slow is fast:# 如果快慢指针相遇为环形链表
                return True
        return False
