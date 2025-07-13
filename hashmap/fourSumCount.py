class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        # O(N^2) time complexity 
        d = {}
        count = 0
        
        for i in nums1:
            for j in nums2:
                d[(i+j)] = d.get((i+j),0) + 1
                
        for i in nums3:
            for j in nums4:
                count += d.get(-(i+j), 0)
        
        return count
