from collections import Counter 

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = Counter(s)
        #print(c)
        for index, elem in enumerate(s):
            if c[elem] == 1:
                return index    
        return -1
