'''
用两个哈希表存储每个字符出现次数，之后进行比较
空间复杂度O(1)，时间复杂度O(n)
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap1, hashMap2 = {}, {}
        for x in s:
            hashMap1[x] = hashMap1.get(x, 0) + 1
        for x in t:
            hashMap2[x] = hashMap2.get(x, 0) + 1
        return hashMap1 == hashMap2
