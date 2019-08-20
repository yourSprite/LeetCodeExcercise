'''
哈希表存储每个字符出现次数
空间复杂度O(n)，时间复杂度O(n)
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        index = 0
        for chr in s:
            if count[chr] == 1:
                return index
            else:
                index += 1
        return -1
