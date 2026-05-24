class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m_p = 1000000000
        profit = 0
        
        for p in prices:
            m_p = min(p, m_p)
            profit = max(profit, p - m_p)
        return profit
            
        