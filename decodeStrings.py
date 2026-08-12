from collections import defaultdict

class Solution:
    def decodeString(self, s: str) -> str:
        result = ""
        d = defaultdict(str)

        val = ""
        l,r = 0,0

        # "3[a]2[bc]"
        while s:
            if s[l].isdigit():
                val += s[l]
                r += 1
            if char[l] in ['[']:
                r += 1


            

            


        return 

A = Solution()  
s1 = "3[a]2[bc]" # "aaabcbc"
print(A.decodeString(s1))
s2 = "3[a2[c]]" # "accaccacc"
print(A.decodeString(s2))
s3 = "2[abc]3[cd]ef" # "abcabccdcdcdef"
print(A.decodeString(s3))