'''
使用log计算
空间复杂度O(1)，时间复杂度O(1)
'''


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and 4 ** round(math.log(num, 4)) == num
