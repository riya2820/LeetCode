class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for row in range(numRows):
            # The first and last row elements are always 1.
            r = [None for _ in range(row + 1)]
            r[0] = 1
            r[-1] = 1 

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(r) - 1):
                r[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]

            triangle.append(r)

        return triangle
        
