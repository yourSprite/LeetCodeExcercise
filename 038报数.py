'''
通过迭代从第一个数字推导到第n个数字
空间复杂度O(1)，时间复杂度O(n)
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        # 求下一个数字
        def next_num(x):
            _len = len(x)
            x = x + '0' # 防止x[i+1]越界
            i = 0
            count = 1
            res = ''
            while i < _len:
                if x[i] == x[i+1]:
                    count += 1
                else:
                    res = res + str(count) + x[i]
                    count = 1
                i += 1
            return res
        # 通过迭代求下一个数字
        res = '1'
        for i in range(1, n):
            res = next_num(res)
        return res