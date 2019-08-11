'''
使用log计算
空间复杂度O(1)，时间复杂度O(1)
'''


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3 ** round(math.log(n, 3)) == n
