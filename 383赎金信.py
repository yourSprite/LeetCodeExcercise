'''
哈希表
空间复杂度O(1)，时间复杂度O(len(ransomNote)+len(magazine))
'''


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for x in magazine:
            dic[x] = dic.setdefault(x, 0) + 1
        for y in ransomNote:
            temp = dic.get(y)
            if not temp:
                return False
            elif temp > 0:
                dic[y] -= 1
            else:
                return False
        return True
