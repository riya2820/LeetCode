from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in set(t):
            if s.count(i) != t.count(i):
                return i
        '''d = defaultdict(int)

        for char in s:
            d[char] += 1

        for char in t:
            if char in d.keys():
                d[char] -= 1
            else:
                d[char] += 1

        result = ""
        for k, v in d.items():
            if d[k] > 0 or d[k] < 0:
                result += str(k)

        return result'''