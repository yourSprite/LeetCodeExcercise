# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root # 树为空
        
        if root == p or root == q:
            return root # p或q为根节点
        
        left = self.lowestCommonAncestor(root.left, p, q) # 在左子树继续查找
        right = self.lowestCommonAncestor(root.right, p, q) # 在右子树继续查找
        
        if not left: # 如果左子树为空在右子树继续查找
            return right
        elif not right: # 如果右子树为空在左子树继续查找
            return left
        else: # 左右为空返回当前根节点
            return root
        
