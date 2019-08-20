'''
方法一：使用哈希表存储数字出现次数
空间复杂度O(2n)，时间复杂度O(2n)
'''


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count1 = collections.Counter(s)
        count2 = collections.Counter(t)
        for key in count2.keys():
            if count1.get(key) is None:
                return key
            elif count1[key] != count2[key]:
                return key


'''
方法二：t的ASCII码之和减去s的ASCII之和
空间复杂度O(2n)，时间复杂度O(2n)
'''


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum1 = 0
        sum2 = 0
        for chr1 in s:
            sum1 += ord(chr1)
        for chr2 in t:
            sum2 += ord(chr2)
        return chr(sum2 - sum1)
