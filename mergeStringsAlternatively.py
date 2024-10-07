class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=0
        r=0
        result = ""
       
        while l < len(word1):
            if r >= len(word2):
                break    
            result += word1[l] + word2[r]
            l += 1
            r += 1

        # check for remaining letters if any        
        if l<len(word1):
            result += word1[l:]
        if r<len(word2):
            result += word2[r:]
        return result

    
