'''
方法一：弹出和推入数字 & 溢出前进行检查
空间复杂度O(1),时间复杂度O(log(x))，x中大约有log(x)个数字
'''


class Solution:
    def reverse(self, x: int) -> int:
        max = 2 ** 31 - 1
        min = -2 ** 31
        rev = 0
        # 注意python中取余数没有正负号
        if x >= 0:
            while x > 0:
                pop = x % 10
                rev = rev * 10 + pop
                if rev > max:
                    return 0
                else:
                    x = x // 10
            return rev
        else:
            x = abs(x)
            while x > 0:
                pop = x % 10
                rev = rev * 10 + pop
                if -rev < min:
                    return 0
                else:
                    x = x // 10
            return -rev


'''
方法二：使用列表对数字进行翻转
空间复杂度O(2log(x)),时间复杂度O(3log(x))
'''


class Solution:
    def reverse(self, x: int) -> int:
        # 注意python中取余数没有正负号
        if x >= 0:
            flag = 1
        else:
            flag = -1
        x = abs(x)
        l = []
        for i in str(x):
            l.append(i)
        rev = l[::-1]
        rev = int(''.join(rev))
        if -2 ** 31 <= rev * flag <= 2 ** 31 - 1:
            return rev * flag
        else:
            return 0
