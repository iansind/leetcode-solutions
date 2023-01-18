# Problem found at https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 1
        R = 0
        L = 0
        curr_sum = 0
        best = (0, 0, 0)
        while i < len(prices) and R < len(prices):
            if prices[i] < prices[L]:
                L = i
                i += 1
                R = i
                continue
            curr_sum = prices[R] - prices[L]
            if curr_sum > best[0]:
                best = (curr_sum, L, R)
            if curr_sum < 1:
                curr_sum = 0
                i = R
            R += 1
        
        return best[0]
      
