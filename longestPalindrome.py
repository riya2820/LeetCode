def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        pairs = 0
        unpaired_chars = set()
        
        # longest palindrome that can be built with these letters
        # O(N) time complexity 
        # similiar to stack style pair/pop
        
        for char in s:
            if char in unpaired_chars:
                pairs += 1
                unpaired_chars.remove(char)
            else:
                unpaired_chars.add(char)
                
        return 2*pairs+1 if unpaired_chars else pairs*2
