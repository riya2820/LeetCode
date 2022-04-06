class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        #Brute Force: O(N^2) time complexity
        #Hash Map Method: O(N) time complexity
       
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
