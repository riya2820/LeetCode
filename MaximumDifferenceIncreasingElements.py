class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_diff = 0
        curr_min = nums[0] 
        # O(N) time complexity 
        for i in range(1, len(nums)):
            curr_min = min(nums[i], curr_min)
            max_diff = max(nums[i] - curr_min, max_diff)
    
        return max_diff if max_diff > 0 else -1
