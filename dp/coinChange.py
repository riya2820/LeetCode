class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        # Time complexity O(amount*len(coin))
        # Space O(amount); since there is an amount array 
        for a in range(1, amount+1):
            for c in coins:
                if a-c >= 0: #still left to search
                    dp[a] = min(dp[a], dp[a-c]+1)
                    
        return dp[amount] if dp[amount] != amount+1 else -1 #make sure not the default value; if deafult value then that means couldn't find the soln; return -1
