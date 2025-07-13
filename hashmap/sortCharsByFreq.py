from collections import defaultdict

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # store into hashmap
        # order by value
        # return string 
        result = ""
        d = defaultdict(int)
        
        for char in s:
            d[char] += 1
             
        d = (sorted(d.items(), key = lambda x:-x[1])) # reverse = True
        
        for item in d:
            result += item[0]*item[1]
            
        return result
