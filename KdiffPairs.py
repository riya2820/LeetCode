
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 0 
        c = collections.Counter(nums) 
        
        for i in c: 
            if (k >0 and i+k in c) or (k == 0 and c[i] > 1): 
                count += 1
        return count
    
#Medium 
#O(N) Runtime 
#Exaplanation:  i+k so you get unique and not double count values and edge case: c[i] > 1 for k=0 means
#there are mutiple of same element for example 2,2 so then we can update count since diff is 0
