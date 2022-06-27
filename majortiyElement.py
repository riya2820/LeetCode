from collections import defaultdict 

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Hash Map Method: O(N) time complexity
        d = defaultdict(int)
        majorityElement = 0
     
          
        # or just write, d = Counter(nums)
        for num in nums:
            d[num] += 1
            
        for i in d:
            if d[i] > (len(nums)/2):
                majorityElement = i
                
        return majorityElement
        

