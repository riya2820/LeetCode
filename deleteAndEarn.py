from collections import defaultdict 

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #probably some dp method and some recursive logic!
        points = defaultdict(int)
        max_num = 0
        
        for i in nums:
            points[i] += i #freq of that number
            max_num = max(max_num, i)
            
        max_points = [0]* (max_num+1)
        max_points[1] = points[1]
        
        for num in range(2, len(max_points)):
            max_points[num] = max(max_points[num-1], max_points[num-2] + points[num])
            
        return max_points[max_num]
