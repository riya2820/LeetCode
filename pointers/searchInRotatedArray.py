class Solution(object):                       
    def search(self, nums, target):
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if target == nums[mid]:
                return mid
            
            if nums[mid] >= nums[left]:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid
                    
                else:
                    left = mid
            
            else:
                if target >= nums[mid] and target <= nums[right]:
                    left = mid
                else:
                    right = mid
        
        
        if nums[left] == target:
            return left
        
        if nums[right] == target:
            return right
        
        return -1
