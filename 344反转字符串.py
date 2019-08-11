'''
双指针，直接交换两个指针指向的值
空间复杂度O(1)，时间复杂度O(n)
'''


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
