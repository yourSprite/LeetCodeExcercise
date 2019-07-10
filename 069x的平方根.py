'''
方法一：二分法
空间复杂度O(1)，时间复杂度O(log(x))
'''


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l = 0
        r = x
        while l < r:
            mid = l + (r - l) / 2
            square = mid * mid
            if square < x:
                l = mid
            elif square == x or square - x < 0.01:
                return int(mid)
            else:
                r = mid


'''
方法二：牛顿迭代法，迭代公式x = (x + a)/2
空间复杂度O(1)，时间复杂度
'''


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1:
                return int(cur)
