# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            if root.left and root.right: # 左右都有子节点取最小深度
                return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
            elif root.left: # 左右只有一个子节点的情况深度为对应子节点，选取左右最小的那个为当前节点本身
                return self.minDepth(root.left) + 1
            elif root.right:
                return self.minDepth(root.right) +1
            else:
                return 1
        else:
            return 0
