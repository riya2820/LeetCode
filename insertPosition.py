class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
         
        last = len(nums) -1
        
        for i in range(len(nums)-1):
            if nums[i] < target and nums[i+1] > target:
                return i+1
            
        if nums[0] > target:
            return 0
        
        if nums[last] < target:
            return last +1
