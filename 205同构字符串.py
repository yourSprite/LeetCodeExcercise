'''
方法一：使用哈希表存储出现字母对应从序号，相当于对LabelEncoder
空间复杂度O(1)，因为最多只有26个字符*2，时间复杂度O(n)
'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMap1, hashMap2 = {}, {}
        flag = 0
        for i in range(len(s)):
            temp1, temp2 = hashMap1.get(s[i]), hashMap2.get(t[i])
            if temp1 != temp2:
                return False
            if not temp1:
                hashMap1[s[i]], hashMap2[t[i]] = flag, flag
                flag += 1
        return True


'''
方法二：直接比较当前字符第一次出现位置
空间复杂度O(1)，时间复杂度O(nlogn)
'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s.index(s[i]) != t.index(t[i]):
                return False
        return True
