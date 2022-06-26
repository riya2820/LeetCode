class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time complexity O(N*N!)
       
        # Base case 
        if len(nums) <= 1: 
            return [nums]
        else:
            result = []
            for i in range(len(nums)):
                for j in self.permute(nums[:i]+nums[i+1:]):
                    result.append([nums[i]]+j)
            return result
