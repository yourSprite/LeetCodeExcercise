class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        sum = 0
        for i in range(l-1):
            # 如果后一天的价格高于前一天便在后一天卖出
            if prices[i+1] > prices[i]:
               sum += prices[i+1] - prices[i]
        return sum
