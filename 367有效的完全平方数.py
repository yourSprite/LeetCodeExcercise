'''
方法一：二分法
空间复杂度O(1)，时间复杂度O(logn)
'''


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = left + (right - left) // 2
            if pow(mid, 2) > num:
                right = mid - 1
            elif pow(mid, 2) < num:
                left = mid + 1
            else:
                return True
        return False


'''
方法二：利用 1+3+5+7+9+…+(2n-1)=n^2，即完全平方数肯定是前n个连续奇数的和
空间复杂度O(1)，时间复杂度O(n)
'''


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        res = 0
        i = 1
        while res < num:
            res += i
            i += 2
        return res == num
