# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 利用中序遍历，左值小于中间值小于右值
    def isValidBSTHelper(self, root, left=None, right=None):
        '''
        root: 中间比较节点，使用root.val
        left: 左比较节点，使用left.val
        right: 右比较节点，使用right.val
        '''
        if not root: # 二叉树为空
            return True
        if left and left.val >= root.val: # 左侧值应小于中间值
            return False
        if right and right.val <= root.val: # 右侧值应大于中间值
            return False
        # 分别更新右比较节点和左比较节点
        return self.isValidBSTHelper(root.left, left, root) and self.isValidBSTHelper(root.right, root, right)
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTHelper(root)
