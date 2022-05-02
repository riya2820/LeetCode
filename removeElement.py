class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #in-place algorithm 0(1) space 
        i=0
        while(i<len(nums)):
            if(nums[i]==val):
                nums.pop(i)
                i-=1
            i+=1
