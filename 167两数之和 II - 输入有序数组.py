'''
双指针法
空间复杂度O(1)，时间复杂度O(n)，n为数组长度
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        while p1 < p2:
            if numbers[p1] + numbers[p2] < target:
                p1 += 1
            elif numbers[p1] + numbers[p2] > target:
                p2 -= 1
            else:
                return [p1 + 1, p2 + 1]
