'''
方法一：使用列表
空间复杂度O(n^2)，时间复杂度O(n)
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            if num not in res:
                res.append(num)
            else:
                res.remove(num)
        return res.pop()


'''
方法二：使用哈希表
空间复杂度O(n)，时间复杂度O(n)
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if not dic.get(num):
                dic[num] = 1
            else:
                dic.pop(num)
        return dic.popitem()[0]


'''
方法三：数学法
空间复杂度O(2n)，时间复杂度O(2n)
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


'''
方法四：位操作，使用亦或
空间复杂度O(n)，时间复杂度O(1)
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
