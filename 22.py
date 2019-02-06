class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.list = []
        self._gen(0, 0, n, "")
        return self.list


    def _gen(self, left, right, n, result):
        """
        递归函数
        :param left: 左括号已用个数
        :param right: 右括号已用个数
        :param n: 括号对数
        :param result: 当前产生括号对数
        :return:
        """
        if left == n and right == n: # 左右括号都用完
            self.list.append(result)
            return
        if left < n: # 先增加左括号，左括号随时都可以加，例如这里是(，执行后((
            self._gen(left+1, right, n, result+"(")
        if left > right: # 增加右括号，保持左右括号成对出现，例如这里是(，执行后()
            self._gen(left, right+1, n, result+")")
