class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        magh = 0
        magv = 0
        
        for i in moves:
            if i == "L":
                magh -= 1
            if i == "R":
                magh += 1
                
            if i == "U":
                magv -= 1
                
            if i == "D":
                magv += 1
                
        return magh == magv == 0
        
