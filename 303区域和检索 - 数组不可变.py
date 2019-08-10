'''
使用列表存储结果
空间复杂度O(n)，时间复杂度，预计算O(n)，查询O(1)
'''


class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            self.nums = []
            self.nums_sum = []
        else:
            self.nums = nums
            self.nums_sum = [nums[0]]
            for i in range(1, len(nums)):
                self.nums_sum.append(self.nums_sum[i - 1] + nums[i])

    def sumRange(self, i: int, j: int) -> int:
        # 不能直接减nums_sum[i - 1]因为有i=0的情况存在
        return self.nums_sum[j] - self.nums_sum[i] + self.nums[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
