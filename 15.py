class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        length = len(nums)
        for i in range(length-2):
            if i > 0 and nums[i] == nums[i-1]:# 两数相同直接跳过
                continue
            l, r = i+1, length-1# 左右两个数的索引
            while l < r:
                s = nums[i]+nums[l]+nums[r]
                if s < 0: l += 1# 小于移动左数，使和增大
                elif s > 0: r -= 1# 大于移动右数，使和减小
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:# 两数相同直接跳过
                        l += 1
                    while l < r and nums[r] == nums[r-1]:# 两数相同直接跳过
                        r -= 1
                    l += 1;r -= 1# 满足和为0情况下同时移动

        return res
