'''
方法一：
空间复杂度O(1)，时间复杂度O(logn)
'''


class Solution:
    def addDigits(self, num: int) -> int:
        res = float('inf')
        while res > 9:
            res = 0
            while num > 0:
                res += num % 10
                num = num // 10
            num = res
        return res


'''
方法二：
空间复杂度O(1)，时间复杂度O(1)
'''


class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        return (num - 1) % 9 + 1
