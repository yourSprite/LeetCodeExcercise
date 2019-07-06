'''
方法一：递归，两个链表头部较小的一个与剩下元素的merge操作结果合并
空间复杂度O(m+n)，时间复杂度O(m+n)
'''


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


'''
方法二：迭代，向哨兵节点逐一插入两个链表中较小元素，最后合并非空元素
空间复杂度O(1)，时间复杂度O(min(m, n))
'''


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 哨兵节点
        prehead = ListNode(-1)
        prev = prehead
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 else l2
        return prehead.next


'''
方法三：将两个链表转为list，合并排序后再转换为链表
空间复杂度O(m+n)，时间复杂度O(3(m+n))
'''


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        # 处理第一个列表
        list1 = []
        node = l1
        while node:
            list1.append(node.val)
            node = node.next
        # 处理第二个列表
        list2 = []
        node = l2
        while node:
            list2.append(node.val)
            node = node.next
        # 合并两个列表并排序
        list1.extend(list2)
        list1.sort(reverse=True)
        # 将列表转换为链表
        temp = ListNode(list1[0])
        for i in range(len(list1) - 1):
            res = ListNode(list1[i + 1])
            res.next = temp
            temp = res
        return res
