from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """   
        d = defaultdict(int)
        
        for num in nums:
            d[num] += 1
        
        sorted_d_keys = sorted(d, key=d.get, reverse=True) 
        return sorted_d_keys[0:k]
   
