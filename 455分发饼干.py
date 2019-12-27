#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
排序+贪心
空间复杂度O(1)，时间复杂度O(2logn+2n)
'''
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        i, j, res = 0, 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1
        return res
