class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # 1/0 Knapsack 
        # O(m*n) time complexity 
        dp = [[0]*(len(coins)+1) for i in range(amount+1)]
        dp[0] = [1]*(len(coins)+1)

        for a in range(1, amount+1):
            for i in range(len(coins)-1, -1, -1):
                dp[a][i] = dp[a][i+1]
                if a-coins[i] >= 0:
                    dp[a][i] += dp[a-coins[i]][i]

        return dp[amount][0] 
