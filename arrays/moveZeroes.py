class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        temp1, temp2 = 0,0
        l,r = 0,1

        while l < len(nums) and r < len(nums):
            if nums[l] == 0 and nums[r] != 0: # 0, 1
                temp1 = nums[r] # 1
                temp2 = nums[l]
                nums[l], nums[r] = temp1, temp2 
                l += 1
                r += 1
            
            elif nums[l] == nums[r] == 0:
                r += 1

            else:
                l += 1
                r += 1

       # l r           #  l r
nums1 = [0,1,0,3,12] # [1,0,0,3,12] --> [1,3,0,0,12] --> [1,3,12,0,0] 
nums2 = [0]
A = Solution()
print(A.moveZeroes(nums1))