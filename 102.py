# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
方法1、BFS
"""
import collections

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return [] # 根节点为空，返回[]
        
        queue = collections.deque() # 生成一个双端队列，用于保存本层节点
        queue.append(root) # 从第一层开始，存入根节点
        result = [] # 保存结果
        
        # visited = set(queue) # 判断子节点是否已经搜索，这里树不需要，但是图的BFS需要
        
        while queue:
            level_size = len(queue) # 当前层的节点数量
            current_level = [] # 当前层的节点
            
            for _ in range(level_size):
                node = queue.popleft() # 从左侧遍历
                current_level.append(node.val)
                if node.left: queue.append(node.left) # 下一层节点
                if node.right: queue.append(node.right)
            
            result.append(current_level)
                
        return result
        
"""
方法2、DFS
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return [] # 树为空，返回[]
        self.result = [] # 保存结果
        self._dfs(root, 0) # 进行dfs递归
        return self.result
        
    def _dfs(self, node, level):
        if not node: return # 递归终止条件
        
        if len(self.result) < level + 1: # 当前行没有任何结果，增加一个空数组，方便后面累加结果
            self.result.append([])
            
        self.result[level].append(node.val) # 在对应层增加节点
        
        self._dfs(node.left, level + 1) # if node.left: self._dfs(node.left, level + 1)
        self._dfs(node.right, level + 1) # if node.right: self._dfs(node.right, level + 1)
