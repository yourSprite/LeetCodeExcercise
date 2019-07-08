'''
方法一：正向遍历，注意要区分最后几位为空格情况
空间复杂度O(1)，时间复杂度O(n)
'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        length = len(s)
        # res1默认空格后还有字符串，遇到空格归零
        res1 = 0
        # res2用来保存最近的一个字符串长度
        res2 = 0
        i = 0
        while i < length:
            if s[i] == ' ' and i == (length - 1):
                return res2
            elif s[i] == ' ':
                res1 = 0
            else:
                res1 += 1
                res2 = res1
            i += 1
        return res1


'''
方法二：反向遍历，只到遇到最后一位不为空格字母计算长度
空间复杂度O(1)，时间复杂度O(l)，l为最后一个单词首到字符串尾长度
'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        i = len(s) - 1
        # 找到单词
        while i >= 0:
            if s[i] == ' ':
                i -= 1
            elif s[i] != ' ':
                break
            else:
                return 0
        # 输出结果
        res = 0
        while True:
            if i == 0 and s[i] != ' ':
                return res + 1
            elif s[i] != ' ':
                res += 1
                i -= 1
            else:
                return res
