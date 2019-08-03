'''
方法一：迭代除以2
空间复杂度O(1)，时间复杂度O(logn)
'''


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n:
            if n == 1:
                return True
            if n % 2 != 0:
                return False
            n = n // 2
        return True


'''
方法二：二进制中2的幂只有最高位是1
'''


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
