'''
将罗马数字存入哈希表，如果两位匹配返回两位对应值，否则返回一位对应值
空间复杂度O(1),时间度复杂度O(1)
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
               'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
               'X': 10, 'IX': 9, 'V': 5, 'IV': 4,
               'I': 1}
        i = 0
        res = 0
        while i < len(s):
            if s[i:i + 2] in dic:
                res += dic[s[i:i + 2]]
                i += 2
            else:
                res += dic[s[i]]
                i += 1
        return res