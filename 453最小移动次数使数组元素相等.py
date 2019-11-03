'''
利用排序
空间复杂度O(1)，时间复杂度O(nlogn)
'''


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # nums.sort()
        sorted(nums)
        count = 0
        n = len(nums)
        for i in range(n):
            count += nums[n - 1] - nums[i]
        return count
