'''
方法一：使用掩码与第i位比较，比较之后掩码向左移动一位
'''


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        mask = 1
        for i in range(32):
            if mask & n != 0:
                res += 1
            mask <<= 1
        return res


'''
方法二：使用n和n-1做与运算,会把最后一个1变为0
'''


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n != 0:
            res += 1
            n = n & (n - 1)
        return res


'''
方法三：调用函数
'''


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return str(bin(n)).count('1')
