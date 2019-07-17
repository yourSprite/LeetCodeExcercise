'''
动态规划
空间复杂度O(numRows^2)，时间复杂度O(numRows^2)
'''


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1]]
        for i in range(1, numRows):
            l = [1]
            j = 1
            while j < i:
                l.append(res[i - 1][j - 1] + res[i - 1][j])
                j += 1
            l.append(1)
            res.append(l)
        return res
