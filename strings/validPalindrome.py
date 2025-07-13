class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = ''.join(item for item in s if item.isalnum()) 
 
        if (s[::-1] == s):
            return True
        else:
            return False
