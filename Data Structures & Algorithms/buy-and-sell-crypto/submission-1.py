class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i, n):
                p = prices[j] - prices[i]
                if p > 0:
                    profit = max(profit, p)
        return profit
            
        