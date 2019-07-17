# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
方法一：深度优先搜索迭代
空间复杂度O(N)，时间复杂度O(N)，N为节点数量
'''


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        queue = [(0, root)]
        while queue:
            curr_sum, node = queue.pop(0)
            left = node.left
            right = node.right
            if left:
                queue.append((curr_sum + node.val, node.left))
            if right:
                queue.append((curr_sum + node.val, node.right))
            if not left and not right:
                total_sum = curr_sum + node.val
                if total_sum == sum:
                    return True
        return False


'''
方法二：递归
空间复杂度O(N)，时间复杂度O(N)，N为节点数量
'''


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
