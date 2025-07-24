from collections import defaultdict 

class Solution:
    def isIsomorphic(self, s, t):
        d1 = defaultdict(list)
        d2 = defaultdict(list)

        for idx, char in enumerate(s):
            if char in d1:
                d1[char].append(idx)
            else:
                d1[char] = [idx]

        for idx, char in enumerate(t):
            if char in d2:
                d2[char].append(idx)
            else:
                d2[char] = [idx]
        
        return list(d1.values()) == list(d2.values())



s = "egg"
t = "add"

a = "foo"
b = "bar"

A = Solution()
print(A.isIsomorphic(s,t))
print(A.isIsomorphic(a,b))