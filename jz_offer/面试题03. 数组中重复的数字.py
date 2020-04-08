#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File Name: 面试题03. 数组中重复的数字.py
@Create Time: 2020/4/7 09:41
@Author: wangyutian
@Version: 1.0
@Python Version: Python 3.6.4
@Modify Time: 2020/4/7 09:41
'''

'''
使用哈希表
时间复杂度O(n)
空间复杂度O(n)
'''


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        hashMap = {}
        for num in nums:
            if hashMap.get(num):
                return num
            else:
                hashMap[num] = 1
        return -1


'''
原地排序
时间复杂度O(n)
空间复杂度O(1)
'''


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[i] == nums[nums[i]]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1
