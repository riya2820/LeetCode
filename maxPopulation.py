from collections import defaultdict 

class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """    
        d = defaultdict(int)
        
        for log in logs:
            for year in range(log[0],log[1]):
                d[year] += 1
                
        return min([year for year in d if d[year] == max(d.values())])
        
