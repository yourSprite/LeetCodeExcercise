'''
方法一：哈希表
空间复杂度O(n)， 时间复杂度O(n)，n为nums长度
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return counts.most_common(1)[0][0]


'''
方法二：排序后取中间值
空间复杂度O(1)， 时间复杂度O(nlogn)，n为nums长度
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


'''
方法三：Boyer-Moore 投票算法
空间复杂度O(1)， 时间复杂度O(n)，n为nums长度
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
