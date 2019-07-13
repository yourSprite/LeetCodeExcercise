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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []

        def _levelOrderBottom(root, depth):
            if not root:
                return
            if depth == len(res):
                res.insert(0, [])
            res[-(depth + 1)].append(root.val)
            _levelOrderBottom(root.left, depth + 1)
            _levelOrderBottom(root.right, depth + 1)

        _levelOrderBottom(root, 0)
        return res


'''
方法二：迭代
空间复杂度O(N)，时间复杂度O(N)
N为节点数量
'''


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.insert(0, tmp)
        return res