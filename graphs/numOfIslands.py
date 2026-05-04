class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        def dfs(r, c):
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                if grid[r][c] != "1":
                    continue
                grid[r][c] = "-1"  # mark visited
                if r > 0:
                    stack.append((r-1, c))
                if r+1 < len(grid):
                    stack.append((r+1, c))
                if c > 0: 
                    stack.append((r, c-1))
                if c+1 < len(grid[0]):
                    stack.append((r, c+1))

        num_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    num_islands += 1
                    dfs(row, col)

        return num_islands
        
      