'''
采用厄拉多塞筛法
空间复杂度O(n)，时间复杂度O(n)
'''


class Solution:
    def countPrimes(self, n: int) -> int:
        res = 0
        l = [True] * n
        for i in range(2, n):
            if l[i]:
                res += 1
                for j in range(i, n, i):
                    l[j] = False
        return res
