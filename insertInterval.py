class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # Overall O(N) time complexity!
        newStart, newEnd = newInterval
        i = 0
        n = len(intervals)
        result = []
        
        while i<n and newStart > intervals[i][0]:
            result.append(intervals[i])
            i += 1
            
        if not result or result[-1][1] < newStart:
            result.append(newInterval)
            
        else:
            result[-1][1] = max(result[-1][1], newEnd)
        
        
        while i < n:
            interval = intervals[i]
            start, end = interval
            i += 1
            
            # no overlap then add intervals to result
            if result[-1][1] < start:
                result.append(interval)
            # overlap, then merge the intervals 
            else:
                result[-1][1] = max(result[-1][1], end)
        return result
