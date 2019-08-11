'''
使用哈希表存储一个表的数字
空间复杂度O(m+n)，时间复杂度O(m+n)
'''


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        res = []
        for num1 in nums1:
            dic.setdefault(num1, num1)
        for num2 in nums2:
            num = dic.get(num2)
            if num is not None:
                res.append(num)
                del dic[num]
        return res
