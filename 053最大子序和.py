'''
方法一：动态规划，如果当前sum>0，证明sum对sum+nums[i]有正向作用，sum += nums[i]，
否则直接返回sum = nums[i]
空间复杂度O(1)，时间复杂度O(n)
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _sum = nums[0]
        _max = nums[0]
        for i in range(1, len(nums)):
            if _sum > 0:
                _sum += nums[i]
            else:
                _sum = nums[i]
            _max = max(_sum, _max)
        return _max


'''
方法二：分治，将数组从中间分开，最大和有三种情况，在左边，在右边，在中间
左右两侧最大值和普通计算一样，通过迭代处理，在中间部分可以直接计算
空间复杂度O(1)，时间复杂度O(nlog(n)）
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return nums[0]
        else:
            # 计算左侧最大值
            left_max = self.maxSubArray(nums[:n // 2])
            # 计算右侧最大值
            right_max = self.maxSubArray(nums[n // 2:])

        # 计算中间区域最大值
        mid = len(nums) // 2
        # 左侧数据应该从右向左计算取最大和
        lm = 0
        ls = 0
        for i in range(mid - 1, -1, -1):
            ls += nums[i]
            lm = max(lm, ls)
        rm = 0
        rs = 0
        # 右侧数据用该从左向右计算取最大和
        for i in range(mid + 1, len(nums), 1):
            rs += nums[i]
            rm = max(rm, rs)
        # 返回左侧区域，右侧区域，中间连续区域的最大和
        return max(left_max, right_max, lm + nums[mid] + rm)
