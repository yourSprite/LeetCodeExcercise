"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

'''
BFS，使用queue保存相应的层和节点
空间复杂度O(n)，时间复杂度O(n)
'''


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        queue = [(0, root)]
        res = []

        while queue:
            level, node = queue.pop(0)
            if level == len(res):
                res.append([node.val])
            else:
                res[level].append(node.val)

            if node.children:
                for child in node.children:
                    queue.append((level + 1, child))

        return res
