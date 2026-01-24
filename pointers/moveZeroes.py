class Solution: # in-place 
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = 0

        while r < len(nums): # [0,1,0,3,12]
            if nums[r] != 0: # [1, 3, 12, 0, 0] 
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
            r += 1

    
