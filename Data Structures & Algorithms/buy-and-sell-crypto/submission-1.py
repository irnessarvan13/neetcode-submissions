class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = 1
        maxProfit = 0

        while R < len(prices):
            if prices[R] < prices[L]:
                L = R
            else:
                profit = prices[R] - prices[L]
                maxProfit = max(maxProfit, profit)
            R += 1
        return maxProfit
            


