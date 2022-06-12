class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # edge case
        if not nums:
            return 0

        # O(N)
        nums.sort()

        longest_streak = 1
        current_streak = 1

        # O(N) time complexity 
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]: # some edge case
                if nums[i] == nums[i-1]+1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1 # reset current streak to 1

        return max(longest_streak, current_streak)
