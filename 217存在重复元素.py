'''
方法一：哈希表
空间复杂度O(n)，时间复杂度O(n)
'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for num in nums:
            if hashMap.get(num):
                return True
            hashMap[num] = 1
        return False


'''
方法二：使用python集合
空间复杂度O(n)，时间复杂度O(n)
'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


'''
方法三：排序
空间复杂度O(1)，时间复杂度O(nlogn)
'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                return True
        return False
