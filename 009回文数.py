'''
方法一：使用列表反转数字并比较
空间复杂度O(2log(x))，时间复杂度O(2log(x))
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        l = []
        for i in str(x):
            l.append(i)
        rev = ''.join(list(reversed(l)))
        if rev == str(x):
            return True
        return False


'''
方法二：将数字存入列表进行收尾比较
空间复杂度O(log(x))，时间复杂度O(3/2log(x))
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        l = []
        for i in str(x):
            l.append(i)
        length = len(l)
        for i in range(0, length // 2):
            if l[i] != l[-i - 1]:
                return False
        return True


'''
方法三：取出后半段数字进行翻转
空间复杂度O(3/2log(x))，时间复杂度O(1/2log(x))
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 非0数字最后一位为0返回False
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = x // 10
        # 当传入偶数时x == rev//10
        if x == rev or x == rev // 10:
            return True
        else:
            return False
