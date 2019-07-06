'''
方法一：双指针，i为满指针，j为快指针，nums[j]==val跳过，否则nums[i]=nums[j]
空间复杂度O(1)，时间复杂度O(n)
'''


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                j += 1
        return i


'''
方法二：双指针，两个指针分别指向头和尾，如果头指针指向元素等于移除元素，直接和最后一个元素交换，
同时尾指针像前移动，否则头指针向后移动
空间复杂度O(1)，时间复杂度O(n)
'''


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        i = 0
        j = len(nums)
        while i < j:
            if nums[i] == val:
                nums[i] = nums[j - 1]
                j -= 1
            else:
                i += 1
        return i
