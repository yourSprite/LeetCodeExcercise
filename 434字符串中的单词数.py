'''
内置函数
空间复杂度O(n)，时间复杂度O(n)
'''


class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())


'''
空间复杂度O(n)，时间复杂度O(n)
'''


class Solution:
    def countSegments(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            if (i == 0 or s[i - 1] == ' ') and s[i] != ' ':
                res += 1

        return res
