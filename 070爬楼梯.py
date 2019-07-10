'''
方法一：暴力破解法
空间复杂度O(1), 时间复杂度O(2^n)
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climb_Stairs(0, n)

    def climb_Stairs(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        return self.climb_Stairs(i + 1, n) + self.climb_Stairs(i + 2, n)


'''
方法二：记忆化递归。在上一种方法中，计算每一步的结果时出现了冗余。把每一步的结果存储在memo数组之中，
每当函数再次被调用，我们就直接从memo数组返回结果
空间复杂度O(n), 时间复杂度O(n)
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = list(0 for _ in range(n))
        return self.climb_Stairs(0, n, memo)

    def climb_Stairs(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i] = self.climb_Stairs(i + 1, n, memo) + self.climb_Stairs(i + 2, n, memo)
        return memo[i]


'''
方法三：动态规划。dp[i] = dp[i-1] + dp[i+1]
空间复杂度O(1), 时间复杂度O(n)
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = list(0 for _ in range(n + 1))
        if n == 1:
            return 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


'''
方法四：斐波那契数Fib(n) = Fib(n-1) + Fib(n-2)。动态规划中值保留两个数来求下一个数
空间复杂度O(n), 时间复杂度O(n)
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n + 1):
            third = first + second
            first, second = second, third
        return second
