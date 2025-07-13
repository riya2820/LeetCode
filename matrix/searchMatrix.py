class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # time = O(log(n*m)), space = O(1)
        # find target row
        r0 = 0               # top row pointer
        rn = len(matrix) - 1 # bottom row pointer
        while r0 <= rn:
            mid = (r0 + rn) // 2
            if target < matrix[mid][0]:
                rn = mid - 1
            elif target > matrix[mid][-1]:
                ro = mid + 1
            else:
                break
                
        # Now mid if the target row
        targetRow = mid
        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[targetRow][mid]:
                r = mid - 1
            elif target > matrix[targetRow][mid]:
                l = mid + 1
            else:
                return True
        
        return False
