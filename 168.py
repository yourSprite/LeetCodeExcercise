class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 题中已知众数是存在的，那么只需排序后取中间值即可
        l = len(nums)
        nums.sort()
        return nums[l/2]
