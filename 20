class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []# 新建一个栈，用于存储左括号
        paren_map = {')':'(', '}':'{', ']':'['}# 字典用于配对
        for c in s:# 遍历字符串
            if c not in paren_map:# 判断是左括号还是右括号，左括号则放入栈中
                stack.append(c)
            elif not stack or paren_map[c] != stack.pop():# 栈最上字符不匹配右括号，返回False
                return False
        return not stack# 遍历之后判断是否全部配对成功（右括号无冗余）
