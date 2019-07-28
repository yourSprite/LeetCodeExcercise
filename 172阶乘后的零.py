'''
题目简化为求解n!中有多少个5
空间复杂度O(1)，时间复杂度O(logn)
'''


class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n >= 5:
            res += n // 5
            n //= 5
        return res
