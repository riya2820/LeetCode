class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        # O(Nlogn) time 
        arr.sort() # [1,2,3,4]
        min_diff = min(arr[i] - arr[i - 1] for i in range(1, len(arr)))
        # should not include negative 
        result = []
           
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                result.append([arr[i-1],arr[i]])
            
        return result
