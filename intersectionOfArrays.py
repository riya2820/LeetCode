class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #built in intersection; faster but more memory 
        #return list(set(nums1) & set(nums2)) 
        
        #slower, but less memory 
        result = []
        for i in set(nums1):
            if i in set(nums2):
                result.append(i)
        return result
                
