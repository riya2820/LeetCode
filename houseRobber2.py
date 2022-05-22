class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
    
    def helper(self, nums):
        t1 = 0
        t2 = 0
        for num in nums:
            temp = t1
            t1 = max(t1, num+t2)
            t2 = temp
        return t1
