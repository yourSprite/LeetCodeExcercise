# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
方法一：递归
空间复杂度O(N)，时间复杂度O(N)
N为节点数量
'''


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            leftHeight = self.maxDepth(root.left)
            rightHeight = self.maxDepth(root.right)
        return max(leftHeight, rightHeight) + 1


'''
方法二：迭代
空间复杂度O(N)，时间复杂度O(N)
N为节点数量
'''


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        if root:
            stack.append((1, root))
        depth = 0
        while stack:
            currentDepth, root = stack.pop()
            if root is not None:
                depth = max(depth, currentDepth)
                stack.append((currentDepth + 1, root.left))
                stack.append((currentDepth + 1, root.right))
        return depth
