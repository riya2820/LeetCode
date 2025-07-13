class Solution:
    def isPalindrome(self, x: int) -> bool:
       # a = -pow(2,31)
        #b = pow(2,31) -1
        if -2**31 >= x or x >=2**31-1:
            return False
        s = str(x)
        if s[::-1] == s:
            return True
        else:
            return False
