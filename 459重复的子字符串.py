#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
遍历1/2字符串得到子字符串，if 子字符串*n=s，返回True
空间复杂度O(n),时间复杂度O(n/2)
'''


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        i = 1
        while i <= len(s) // 2:
            if s[:i] * (len(s) // i) == s:
                return True
            i += 1
        return False


'''
将两个s拼接，去掉首位，如果字符串还包含s，返回True
空间复杂度O(1)，时间复杂度O(n/2)
'''


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s)[1:-1].find(s) != -1
