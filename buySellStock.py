class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        Solution 1
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
                    profit = max(profit, price - cost)

                return profit
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

       
        
