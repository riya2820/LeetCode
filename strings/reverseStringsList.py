class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        l = s.split( )
        result += ' '.join(l[::-1]).strip()

        return result 
