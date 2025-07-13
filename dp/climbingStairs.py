class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dictionary = {}
        def fib_dp(n):
            if n <= 2:
                return n

            if n not in dictionary:
                dictionary[n] = fib_dp(n - 1) + fib_dp(n - 2)
                return dictionary[n]
            else:
                return dictionary[n]

        return fib_dp(n)
