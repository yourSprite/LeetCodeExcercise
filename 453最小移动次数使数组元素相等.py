'''
利用排序
空间复杂度O(1)，时间复杂度O(nlogn)
'''


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums) - 1
        while n >= 0:
            count += nums[n] - nums[0]
            n -= 1
        return count
