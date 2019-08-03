# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
方法一：迭代
空间复杂度O(n)，时间复杂度O(n)
'''


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


'''
方法二：递归，广度优先搜索（BFS）
空间复杂度O(n)，时间复杂度O(n)
'''


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        queue = [root]
        while queue:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
