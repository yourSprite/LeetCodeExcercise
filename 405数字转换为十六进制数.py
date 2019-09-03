'''
当num<0时加上补码
空间复杂度O(1)，时间复杂度O(logn)
'''


class Solution:
    def toHex(self, num: int) -> str:
        max_int = 0xffffffff + 0x00000001  # 补码
        if num < 0:
            num += max_int

        if num == 0:
            return '0'

        hex_convert = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        quotient = num  # 被除数
        divisor = 0x00000010  # 除数
        res = ''

        while quotient:
            quotient, remainder = divmod(quotient, divisor)
            res = hex_convert[remainder] + res

        return res
