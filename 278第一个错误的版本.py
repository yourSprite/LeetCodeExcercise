# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

'''
二分法：
空间复杂度O(1)，时间复杂度O(logn)
'''


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        return left
