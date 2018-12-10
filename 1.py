class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}# 哈希表存储数组下标及元素
        res = []# 存储返回结果
        for i, x in enumerate(nums):# 遍历数组
            if target-x in hashMap.values():# 如果存在与当前值匹配元素
                # 匹配元素下标
                res.append(list(hashMap.keys())[list(hashMap.values()).index(target-x)])
                # 当前值下标
                res.append(i)
                return res
            hashMap[i] = x# 没有匹配元素则将当前值及下标存入哈希表
            
