'''
方法一：排序遍历
空间复杂度O(1)，时间复杂度O(nlogn)
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)


'''
方法二：哈希表
空间复杂度O(n)，时间复杂度O(n)
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i


'''
方法三：用所有数的和减去列表中数的和
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums_sum = 0
        for num in nums:
            nums_sum += num
        return (1 + n) * n // 2 - nums_sum
