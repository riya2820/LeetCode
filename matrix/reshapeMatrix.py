class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # 2x2 --> 1x4 
        rows = len(mat)
        cols = len(mat[0])
        
        # Edge case 
        if not mat: 
            return mat
        
        # if matrix cannot be transformed
        if rows*cols != r * c:
            return mat
        
        # create resulting matrix 2D -> 1D
        result = [[0 for i in range(c)] for i in range(r)] # [[0,0,0,0]]

        # 1D -> 2D
        # convert back to 2D with new dimensions 
        i = 0
        while i < r*c:
            # i % c -> current column number
            # i// c-> # of rows we have completely filled
            result[i//c][i%c] = mat[i//cols][i%cols]
            # result[0][0], result[0][1], result[0][2], result[0][3]
            i += 1
            
        return result  
