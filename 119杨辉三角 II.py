'''
动态规划，只保存上一行的数组
空间复杂度O(2k-1)，时间复杂度O(k^2)，k为行数
'''


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1]
        pre = [1]
        for i in range(1, rowIndex + 1):
            l = [1]
            j = 1
            while j < i:
                l.append(pre[j - 1] + pre[j])
                j += 1
            l.append(1)
            pre = l
        return l
