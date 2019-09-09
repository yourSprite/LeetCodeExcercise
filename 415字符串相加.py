'''
空间复杂度O(1)，时间复杂度O(N)
'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        point1, point2 = len(num1) - 1, len(num2) - 1
        tmp = 0
        res = ''

        while point1 >= 0 or point2 >= 0:
            n1 = int(num1[point1]) if point1 >= 0 else 0
            n2 = int(num2[point2]) if point2 >= 0 else 0
            n = n1 + n2 + tmp
            if n > 9:
                res = str(n - 10) + res
                tmp = 1
            else:
                res = str(n) + res
                tmp = 0
            point1 -= 1
            point2 -= 1

        if tmp == 1:
            return '1' + res
        else:
            return res
