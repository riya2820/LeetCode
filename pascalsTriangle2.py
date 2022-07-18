class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # O(N) time and space 
        result = []
        
        for row in range(rowIndex+1):
            r = [None for i in range(row+1)]
            r[0] = 1
            r[-1] = 1

            for j in range(1, len(r)-1):
                r[j] = result[row-1][j] + result[row-1][j-1]
                
            result.append(r)
        
        return result[rowIndex]

