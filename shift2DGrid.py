def shiftGrid(grid, k):
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: List[List[int]]
    """
    num_rows = len(grid)
    num_cols = len(grid[0])

    for i in range(k):  # do this k times
        # new grid with all cells 0
        new_grid = [[0] * num_cols for i in range(num_rows)]

        # Move everything not in the last column.
        for row in range(num_rows):
            for col in range(num_cols - 1):
                new_grid[row][col + 1] = grid[row][col]

        # Move everything in last column (except last row!)
        for row in range(num_rows - 1):
             new_grid[row + 1][0] = grid[row][num_cols - 1]

        # Move the bottom right 
        new_grid[0][0] = grid[num_rows - 1][num_cols - 1]

        grid = new_grid

    return grid
    
# Sample Test Case:
#print(shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 1))
