'''
方法一：抽屉原理+基于亦或运算交换两个变量的值
空间复杂度O(1)，时间复杂度O(N)
'''


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 亦或运算交换两个变量的值
        def swap(nums, index1, index2):
            # 两个索引相同不交换
            if index1 == index2:
                return
            nums[index1] = nums[index1] ^ nums[index2]
            nums[index2] = nums[index1] ^ nums[index2]
            nums[index1] = nums[index1] ^ nums[index2]

        for i in range(len(nums)):
            # 如果不在位置上，并且它要去的位置上的数不等于自己,则交换
            while nums[i] != nums[nums[i] - 1]:
                swap(nums, i, nums[i] - 1)
        return [i + 1 for i, num in enumerate(nums) if num != i + 1]


'''
方法二：将数组的value作为下标，更改对应下标的数值符号
空间复杂度O(1)，时间复杂度O(N)
'''


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        return [i + 1 for i, num in enumerate(nums) if num > 0]
