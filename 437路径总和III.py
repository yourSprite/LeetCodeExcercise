# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
双重递归
空间复杂度(nlogn)，时间复杂度O(n)
'''


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        return self.paths(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def paths(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        res = 0

        if root.val == sum:
            res += 1

        res += self.paths(root.left, sum - root.val)
        res += self.paths(root.right, sum - root.val)

        return res
