class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = 0 
        for i in range(1, len(nums)):
            if nums[i] == 0:
                



nums1 = [0,1,0,3,12] # [1,3,12,0,0]
nums2 = [0]