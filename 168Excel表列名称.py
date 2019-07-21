'''
将数字转化为26进制数
空间复杂度O(n)，时间复杂度O(n/26)
'''


class Solution:
    def convertToTitle(self, n: int) -> str:
        ASCII_A = ord('A')
        res = ''
        while n:
            num = n % 26
            if num == 0:
                res = 'Z' + res
            else:
                res = chr(num - 1 + ASCII_A) + res
            n = (n - 1) // 26
        return res
