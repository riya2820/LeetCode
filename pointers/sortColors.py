class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # colors: red, white, blue
        # use 3 pointers to sort
        # lets say p1 -> red and p2
        # now red is sorted; p2 and p3 will sort the remaining 2 colors
        # p2-> white, p3-> blue 
        
        # 3 pointers; can also call it low, middle, high
        p1 = 0
        p2 = 0
        p3 = len(nums)-1
        
        while p2 <= p3 :
            if nums[p2] == 0 :
                nums[p1], nums[p2] = nums[p2], nums[p1] # shorthand of swap function
                p1 += 1
                p2 += 1
                
            elif nums[p2] == 1 :
                p2 += 1
            else:
                nums[p2], nums[p3] = nums[p3], nums[p2]
                p3 -= 1
            
        return nums
        
