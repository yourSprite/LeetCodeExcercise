# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
方法一：递归
空间复杂度，O(N)，用于维护递归栈，时间复杂度O(N)
N为节点数量
'''


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        elif node1.val != node2.val:
            return False
        return self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left)


'''
方法二：迭代。每次提取两个结点并比较它们的值。然后，将两个结点的左右子结点按相反的顺序插入队列中。
空间复杂度，O(N)，用于维护递归栈，时间复杂度O(N)
N为节点数量
'''


class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        queue = [root.left, root.right]
        while queue:
            node1 = queue.pop(0)
            node2 = queue.pop(0)
            if not node1 and not node2:
                continue
            elif not node1 or not node2:
                return False
            elif node1.val != node2.val:
                return False
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        return True
