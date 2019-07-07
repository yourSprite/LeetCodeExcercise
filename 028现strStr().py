'''
方法一：暴力破解法
空间复杂度O(1)，时间复杂度O((m-n)n)，m为haystack长度，n为needle长度
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        elif len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            j = 0
            if haystack[i] == needle[j]:
                while True:
                    j += 1
                    if i + j >= len(haystack) and j < len(needle):
                        return -1
                    elif j >= len(needle):
                        return i
                    elif haystack[i + j] != needle[j]:
                        break
        return -1

'''
方法二：使用内置函数
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)