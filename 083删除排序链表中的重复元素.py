# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
方法一：由于给定排序列表，可以直接比较当前节点值与下个节点值是否相同
空间复杂度O(1)，时间复杂度O(n)
'''


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


'''
方法二：考虑未排序方法，使用哈希表存储已经出现的数字
空间复杂度O(n)，时间复杂度O(n)
'''


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dict = {}
        cur = head
        pre = head
        while cur is not None:
            if dict.get(cur.val):
                pre.next = cur.next
            else:
                dict[cur.val] = 1
                pre = cur
            cur = cur.next
        return head
