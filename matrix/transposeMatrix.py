class Solution:
    def transpose(self, matrix):
        #edge case handling
        if not matrix or not matrix[0]:
            return []
            
        result = []
        rows = len(matrix)
        cols = len(matrix[0])

        for c in range(cols):
            temp = []
            for r in range(rows):
                temp.append(matrix[r][c])
            result.append(temp)

        return result'''


# Transpose (i.e cols become rows!)
# 1 2 3     1 4 7
# 4 5 6  -> 2 5 6
# 7 8 9     3 6 9
A = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(A.transpose(matrix))

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(A.transpose(matrix))