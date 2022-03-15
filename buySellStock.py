class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        Solution 1
        max_ = 0
        min_ = prices[0]
        for price in prices:
            min_ = min(min_, price)
            profit = price - min_
            max_ = max(max_, profit)
        return max_
        """
        #Solution 2
        #faster runtime time and lesser memory than method1
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right #if buy is greater i.e loss then move left and right                               ahead 
            right += 1
        return max_profit

       
        
