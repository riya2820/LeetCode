from collections import defaultdict 

class Solution:
    def reverseVowels(self, s):
        d = defaultdict(list)

        for idx,char in enumerate(s):
            print(idx, char)
            '''
            if char in d.keys():
                d[char].append(idx)
            else:
                d[char] = [idx]
        '''
        print(d)
        return 
        


# Test Cases
s1 = "IceCreAm" # --> : "AceCreIm"
s2 = "leetcode" # -->  "leotcede"

A = Solution()
print(A.reverseVowels(s1))
# print(A.reverseVowels(s12))