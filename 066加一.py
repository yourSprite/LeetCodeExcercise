'''
直接判断当前位数，9变为0前一位接着加一，其他直接加一返回
空间复杂度O(1)，时间复杂度O(n)，n为digits长度
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        while i > 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                i -= 1
        if digits[0] == 9:
            digits[0] = 0
            digits.insert(0, 1)
        else:
            digits[0] += 1
        return digits