'''
方法一：1.n转为二进制并去掉前缀0b
       2.将二进制数字左侧填0补齐32位
       3.反转二进制
       4.转为十进制
'''


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n)[2:].zfill(32)[::-1], base=2)


'''
方法二：二进制移位
取出 n 的最低位，加入结果 res 中。然后 n 右移，res 左移。循环此过程
'''


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        count = 32
        while count:
            res <<= 1
            res += n & 1
            n >>= 1
            count -= 1
        return res
