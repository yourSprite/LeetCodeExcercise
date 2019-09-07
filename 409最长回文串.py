'''
方法一：使用字典保存每个字母出现次数，再进行两两配对
空间复杂度O(1)，时间复杂度O(N)
'''


class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashMap = {}
        res = 0
        for x in s:
            if hashMap.get(x) is None:
                hashMap[x] = 1
            else:
                hashMap[x] += 1

        for value in hashMap.values():
            res += 2 * (value // 2)

        if res < len(s):
            return res + 1
        else:
            return res


'''
方法二：使用collections.Counter统计每个字母出现次数
空间复杂度O(1)，时间复杂度O(N)
'''

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        res = 0

        for value in counter.values():
            res += 2 * (value // 2)
        if res < len(s):
            return res + 1
        else:
            return res
