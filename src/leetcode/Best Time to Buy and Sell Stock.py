class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy = prices[0]

        for i in prices:
            buy = min(buy, i)
            profit = max(profit, i - buy)
        return profit
        