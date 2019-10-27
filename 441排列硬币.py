from math import sqrt, floor

'''
等差数列求和公式求解
空间复杂度O(1)，时间复杂度O(1)
'''


class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = floor((-1 + sqrt(1 + 8 * n)) / 2)
        return res


'''
二分法
空间复杂度O(1)，时间复杂度O(logn)
'''


class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        l, r = 1, n
        while l < r:
            mid = l + (r - l) // 2
            target = (1 + mid) * mid / 2
            if n - target < 0:
                r = mid
            elif n - target > mid:
                l = mid
            else:
                return mid
        return l
