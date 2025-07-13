class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        cost = prices[0]
        
        for price in prices:
            cost = min(price, cost)
            profit += price - cost
            cost = price
        return profit 
        
       
