class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 1, 1                                        # O(N) time 
        # 0, 0, 1, 1, 1, 2, 2, 3, 3, 4
                                                           # l  r
        while r < len(nums):                               # 0, 0, 1, 1, 1, 2,
            if nums[r] != nums[r-1]:                       # 0, 0, 1, 1, 1, 2,
                nums[l] = nums[r]                          # 1, 2, 1, 1 
       
                l += 1
            r += 1

        return l  

    #  nums = [3,2,2,3], val = 3
    def removeElement(self, nums: List[int], val: int) -> int:
       l, r = 1, 1  
       while r < len(nums):                               #  3, 2, 2, 3
            if nums[r] == val:                            # l,r
                nums[l] = nums[r]                         # 2, 2, 2, 3
                l += 1                                    #    l     r
            r += 1

        return l  

    def merge(self, nums1: List[int], m: int, nums2: List[int], n):
        # Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        # Output: [1,2,2,3,5,6]
        # length = len(nums1)
        # [1,2,3, 0, 0, 0]
        #         -  -  -
        # [2,5,6]
        #  - - -
        last = m + n -1 # index: 0,1,2,3,4,5 (last)
        #          0 1 2 3 <- last
        # nums1 = [1,2,3,0,0,0]  
        # nums2 = [2, 5, 6]

        # merge in reverse order 
        while m > 0 and n > 0: # m=3,n=3
            #   1 > 2 
            if nums1[m-1] > nums2[n-1]:  
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1 # [1,2,3,2,5,6] 
            last -= 1 

        while n > 0:
            nums1[last] = nums2[n-1]
            n = n-1
            last = last-1

   

