class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # O(N*2^N) runtime
        n = len(nums)
        result = [[]]
        
        
        for num in nums:
            result += [curr+[num] for curr in result]
            
        return result
