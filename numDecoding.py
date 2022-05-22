class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 2 and s[0] == "0":
            return 0
        
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        
        dp[1] = 0 if s[0] == '0' else 1
        
        for i in range(2, len(dp)):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
                
            twoDigit = int(s[i-2: i])
            if twoDigit >= 10 and twoDigit <= 26:
                dp[i] += dp[i-2]
            
        return dp[len(s)]
