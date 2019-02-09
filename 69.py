class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        
        # 二分法
        l = 0
        r = x
        
        while l <= r:
            m = (l + r) // 2
            if m == x // m:
                return m
            elif m < x // m:
                l = m + 1
                res = m
            else:
                r = m - 1
                
        return res
