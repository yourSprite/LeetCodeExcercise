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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += '->'
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, '')
        return paths


'''
方法二：递归
空间复杂度O(n)，时间复杂度O(n)
'''


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        paths = []
        queue = [(root, str(root.val))]
        while queue:
            node, path = queue.pop(0)
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                queue.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                queue.append((node.right, path + '->' + str(node.right.val)))
        return paths
