'''
方法一：暴力法
空间复杂度O(1)，时间复杂度O(n^2)
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > res:
                    res = prices[j] - prices[i]
        return res


'''
方法二：一次遍历
空间复杂度O(1)，时间复杂度O(n)
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        res = 0
        for price in prices:
            if price < min_price:
                min_price = price
            res = max(res, price - min_price)
        return res
