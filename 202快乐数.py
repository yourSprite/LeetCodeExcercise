'''
使用哈希表存储已有的数字
'''


class Solution:
    def isHappy(self, n: int) -> bool:
        hashMap = {}
        m = 0
        while True:
            while n != 0:
                m += pow((n % 10), 2)
                n = n // 10
            if m == 1:
                return True
            if hashMap.get(m):
                return False
            hashMap[m] = 1
            n, m = m, 0
