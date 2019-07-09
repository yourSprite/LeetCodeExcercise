'''
方法一：从两个数字末尾进行相加，正向存储，最后再将字符串反转（注意最后一位如果进位要加1）
空间复杂度O(1)，时间复杂度O(m+n),m和n为两个字符串长度
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        res = ''
        # 标志位记录是否进位
        flag = 0
        while i >= 0 or j >= 0:
            a_str = int(a[i]) if i >= 0 else 0
            b_str = int(b[j]) if j >= 0 else 0
            if a_str + b_str == 2:
                res += str(flag)
                flag = 1
            elif a_str + b_str + flag == 2:
                res += '0'
                flag = 1
            else:
                res += str(a_str + b_str + flag)
                flag = 0
            i -= 1
            j -= 1
        if flag == 1:
            res += '1'
        return res[::-1]


'''
方法二：将两个数字转换为十进制相加再转回二进制
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
