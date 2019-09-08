'''
空间复杂度O(1)，时间复杂度O(N)
'''


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = float('-inf')
        second = float('-inf')
        third = float('-inf')

        for num in nums:
            if num == first or num == second or num == third:
                pass
            elif num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num

        if third > float('-inf'):
            return third
        else:
            return first
