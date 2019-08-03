'''
使用哈希表
空间复杂度O(n)，时间复杂度O(n)
'''


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        for i in range(len(nums)):
            idx = hashMap.get(nums[i])
            if idx is not None:
                hashMap[nums[i]] = i
                if (i - idx) <= k:
                    return True
            hashMap[nums[i]] = i
        return False
