'''
哈希表存储映射
空间复杂度O(logn)，时间复杂度O(n)
'''


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        list_str = str.split(' ')
        if len(pattern) != len(list_str):
            return False
        hashMap_pattern = {}
        hashMap_str = {}
        for i in range(len(list_str)):
            flag1 = hashMap_str.setdefault(list_str[i], i)
            flag2 = hashMap_pattern.setdefault(pattern[i], i)
            if flag1 != flag2:
                return False
        return True
