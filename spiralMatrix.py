class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        
        rows = len(matrix)
        cols = len(matrix[0])
        right = cols -1
        down = rows - 1
        up = 0
        left = 0
        
        while len(result) < rows*cols:
            for col in range(left, right+1):
                result.append(matrix[up][col])
                
            for row in range(up+1, down+1):
                result.append(matrix[row][right])
             
            if up != down:
                for col in range(right-1, left-1,-1):
                    result.append(matrix[down][col])
              
            if left != right:
                for row in range(down-1, up,-1):
                    result.append(matrix[row][left])
                
            left += 1
            right -= 1
            up += 1
            down -= 1
                
        return result
