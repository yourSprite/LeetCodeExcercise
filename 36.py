# import numpy as np

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 生成三个三维数组，用于保存数字矩阵[[数字][出现次数]]
        rows = [[0 for _ in range(9)] for _ in range(9)]
        cols = [[0 for _ in range(9)] for _ in range(9)]
        boxes = [[0 for _ in range(9)] for _ in range(9)]

        # rows = np.zeros((9, 9))
        # cols = np.zeros((9, 9))
        # boxes = np.zeros((9, 9))

        for i in range(9): # 遍历行
            for j in range(9): # 遍历列
                num = board[i][j]
                if num != '.':
                    num = int(num) - 1
                    box_index = (i // 3) * 3 + j // 3 # 将9x9数独转换为9个3x3子数独，编号0-9

                    rows[i][num] = rows[i][num] + 1 # 将行中对应出现次数+1
                    cols[j][num] = cols[j][num] + 1
                    boxes[box_index][num] = boxes[box_index][num] + 1

                    if rows[i][num] > 1 or cols[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True
