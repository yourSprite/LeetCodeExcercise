'''
动态规划，选取max(dp[n-1]和dp[n-2]+dp[n])作为dp[n]
空间复杂度O(1)，时间复杂度O(n)
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_max, curr_max = 0, 0
        for i in range(len(nums)):
            temp = curr_max
            curr_max = max(curr_max, prev_max + nums[i])
            prev_max = temp
        return max(prev_max, curr_max)


'''
另一种写法
空间复杂度O(n)，时间复杂度O(n)
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0 for _ in range(len(nums) + 1)]
        dp[-1], dp[0] = 0, nums[0]
        n = 1
        while n < len(nums):
            dp[n] = max(dp[n - 1], dp[n - 2] + nums[n])
            n += 1
        return max(dp[n - 1], dp[n])
