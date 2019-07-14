# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
方法一：递归，注意要分有无左右子树判断，不能简单取min
空间复杂度O(N)，时间复杂度O(N)
N为节点数量
'''


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif root.left:
            return self.minDepth(root.left) + 1
        elif root.right:
            return self.minDepth(root.right) + 1
        else:
            return 1


'''
方法二：深度优先搜索迭代
空间复杂度O(N)，时间复杂度O(N)
N为节点数量
'''


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [(1, root)]
        min_depth = float('inf')
        while queue:
            depth, node = queue.pop(0)
            children = [node.left, node.right]
            if not any(children):
                min_depth = min(depth, min_depth)
            for c in children:
                if c:
                    queue.append((depth + 1, c))
        return min_depth


'''
方法三：广度优先搜索迭代
空间复杂度O(N)，时间复杂度O(N)
N为节点数量
'''


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [(1, root)]
        while queue:
            depth, node = queue.pop(0)
            children = [node.left, node.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    queue.append((depth + 1, c))
