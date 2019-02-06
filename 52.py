class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1: return 0 # 没有皇后时返回空列表

        self.result = [] # 结果列表
        self.cols = set() # 已有皇后占领的列
        self.pie = set() # 已有皇后占领的对角线
        self.na = set()
        self._dfs(n, 0, [])

        return len(self.result)

    def _dfs(self, n, row, cur_state):
        """
        迭代函数
        :param n: n个皇后
        :param row: 行数
        :param cur_state: 当前情况下的皇后位置
        """
        if row >= n: # 遍历行后将当前皇后位置存入结果列表
            self.result.append(cur_state)
            return

        for col in range(n):
            # 如果当前列及对角线已有皇后占领，则继续执行下次循环
            if col in self.cols or row+col in self.pie or row-col in self.na:
                continue

            # 更新皇后已占领的列及对角线
            self.cols.add(col)
            self.pie.add(row+col)
            self.na.add(row-col)

            # 递归下一行
            self._dfs(n, row+1, cur_state+[col])

            # 清除皇后占领位置
            self.cols.remove(col)
            self.pie.remove(row+col)
            self.na.remove(row-col)
