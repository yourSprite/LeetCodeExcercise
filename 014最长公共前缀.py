'''
方法一：水平扫描法，以第一个单词为前缀，依次遍历字符串，如果没有匹配上前缀-1
空间复杂度O(1)，时间复杂度O(S)，S为所有字符串长度和
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or strs is None:
            return ''
        prefix = strs[0]
        for i in range(len(strs) - 1):
            while strs[i + 1].find(prefix) != 0:
                prefix = prefix[0:len(prefix) - 1]
        return prefix


'''
方法er：水平扫描，取每个单词同一位置，看是否相同
空间复杂度O(1)，时间复杂度(S)
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or strs is None:
            return ''
        prefix = ''
        flag = 1
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i < len(strs[j]):
                    if strs[0][i] != strs[j][i]:
                        flag = 0
                        break
                else:
                    flag = 0
                    break
            if flag == 0:
                break
            prefix = prefix + strs[0][i]
        return prefix


'''
方法三：水平扫描，取每个单词同一位置，看是否相同（利用python的zip方法）
空间复杂度O(S)，时间复杂度(2S)
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or strs is None:
            return ''
        prefix = ''
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                prefix += tmp[0]
            else:
                break
        return prefix
