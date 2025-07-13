class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 00 01 02
        # 10 11 12
        # 20 21 22
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col], matrix[col][row]=matrix[col][row], matrix[row][col]
            
        print(matrix)
        
        for row in matrix:
            i = 0
            j = len(d)
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        #reverse every element in each row
        for row in matrix:
            l = 0
            r = len(row) - 1
            while l < r:
                row[l], row[r] = row[r], row[l]
                l += 1
                r -= 1
