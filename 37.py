class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0: return
        self.solve(board)

    def solve(self, board):
        """
        填充数字
        """
        for i in range(9): # 遍历行
            for j in range(9): # 遍历列
                if board[i][j] == '.': # 当前格子需要填充
                    for c in range(1, 10): # 从1开始填充，后续判断是否有效
                        c = str(c) # 将数字转换字符串
                        if self.isValid(board, i, j, c): # 判断是否有效，有效填充数字
                            board[i][j] = c
                            if self.solve(board): # 填充数字后进行递归继续填充数独
                                return True
                            else:
                                board[i][j] = '.' # 后续无法填充进行回溯
                    return False
        return True

    def isValid(self, board, row, col, c):
        """
        判断填入数字是否有效
        """
        for i in range(9):
            if board[i][col] != '.' and board[i][col] == c: # 当前列是否有重复数字
                return False
            if board[row][i] != '.' and board[row][i] == c: # 当前行是否有重复数字
                return False
            if board[3*(row//3)+i//3][3*(col//3)+i%3] != '.' and board[3*(row//3)+i//3][3*(col//3)+i%3] == c:
                # 当前3x3子数独是否有重复数字
                return False
        return True
