'''
空间复杂度O(1)
'''


class Solution:
    def findNthDigit(self, n: int) -> int:
        i, max_count = 0, 0
        while max_count < n:
            i += 1
            max_count += i * (9 * 10 ** (i - 1))
        start_count = max_count - i * (9 * 10 ** (i - 1))
        power = i - 1
        start_val = 10 ** power
        step = n - start_count - 1
        step_length = i
        offset, pos = divmod(step, step_length)
        curr_val = start_val + offset
        result = curr_val // 10 ** (power - pos) % 10
        return result
