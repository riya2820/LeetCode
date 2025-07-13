# Binary Search solution to optimize runtime 
# Takes O(N) time!
# Current method takes O(NLogN) time!
import math 

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        points.sort(key=self.squared_dist) #O(NLogN)
        return points[:k]
        
    def squared_dist(self, point):
        return math.sqrt(point[0]**2 + point[1]**2)
