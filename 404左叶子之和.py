# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
BFS
空间复杂度O(1)，时间复杂度O(n)
'''


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        node_list = [root]
        while node_list:
            node = node_list.pop(-1)
            if node.left and not node.left.left and not node.left.right:
                res += node.left.val
                node_list.append(node.left)
            elif node.left:
                node_list.append(node.left)
            if node.right:
                node_list.append(node.right)
        return res


'''
DFS
空间复杂度O(n)，时间复杂度O(n)
'''


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
