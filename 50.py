class Solution(object):
    def myPow(self, x, n):
        """
        使用迭代计算
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2: # n是奇数
            return x * self.myPow(x*x, n/2) # x * self.mypow(x*x, (n-1)/2)
        else:
            return self.myPow(x*x, n/2)
