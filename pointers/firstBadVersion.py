# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        last = n
        
        while first <= last:
            mid = first + (last - first) // 2
            
            if not isBadVersion(mid):
                first = mid + 1
            else:
                last = mid - 1
                
        return first
       # Optimize to O(logn) time using Binary Search!
        
