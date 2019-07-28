'''
使用环状替换，取余数后直接替换
空间复杂度O(1)，时间复杂度O(n)
'''


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1 or len(nums) == 0:
            pass
        else:
            while k > len(nums):
                k %= len(nums)
            nums[:] = nums[-k:] + nums[:-k]
