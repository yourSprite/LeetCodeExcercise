'''
使用哈希表保存nums1中数字出现次数，然后遍历nums2中数字进行对比，
如果再nums1中出现次数大于1，则nums1的次数减一，等于1删除该数字
空间复杂度O(m+n)，时间复杂度O(m+n)
'''


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        res = []
        for num1 in nums1:
            num = dic.get(num1)
            if num is not None:
                dic[num1] += 1
            else:
                dic[num1] = 1
        for num2 in nums2:
            num = dic.get(num2)
            if num is not None and num > 1:
                res.append(num2)
                dic[num2] -= 1
            elif num is not None and num == 1:
                res.append(num2)
                del dic[num2]
        return res
