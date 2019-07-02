'''
解法一：暴力循环
空间复杂度O(1)，时间复杂度O(n^2)
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(l):
            j = i
            while j < l:
                j += 1
                if nums[i] + nums[j] == target:
                    return [i, j]


'''
解法二：两遍哈希表
空间复杂度O(n)，时间复杂度O(n)
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, num in enumerate(nums):
            dic[num] = i

        for i, num in enumerate(nums):
            j = dic.get(target - num)
            if j is not None and i != j:
                return [i, j]


'''
方法三：一遍哈希表
空间复杂度O(n)，时间复杂度O(n)
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, num in enumerate(nums):
            if dic.get(target - num) is not None:
                return [i, dic.get(target - num)]
            dic[num] = i
