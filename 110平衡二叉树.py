# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
方法一：自顶向下
空间复杂度O(N^2)，时间复杂度O(N)
N为节点数量
'''


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) < 2 and self.isBalanced(
            root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

'''
方法二：自底向上
空间复杂度O(N)，时间复杂度O(N)

'''
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True
        self.helper(root)
        return self.res
    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left) + 1
        right = self.helper(root.right) + 1
        if abs(left - right) > 1:
            self.res = False
        return max(left, right)