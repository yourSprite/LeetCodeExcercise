'''
二十六进制转十进制
空间复杂度O(1),时间复杂度O(n)
'''


class Solution:
    def titleToNumber(self, s: str) -> int:
        ASCII_A = ord('A')
        res = 0
        pointer = len(s) - 1
        i = 1
        while pointer >= 0:
            res += (ord(s[pointer]) - ASCII_A + 1) * i
            i *= 26
            pointer -= 1
        return res
