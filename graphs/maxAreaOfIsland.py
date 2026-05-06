class Solution:
    def maxAreaOfIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 

        rows = len(grid)
        cols = len(grid[0])
        area = 0
        count = 0

        def dfs(r,c):
            print("Line 12")
            stack = [(r, c)]
            area = 0
            count = 0
            while stack:
                r, c = stack.pop()
                if grid[r][c] != 1:
                    continue
                grid[r][c] = -1 # mark visited
                count += 1

                if r > 0:
                    stack.append((r-1, c)) # left 
                if r+1 < len(grid):
                    stack.append((r+1, c)) # right
                if c > 0: 
                    stack.append((r, c-1)) # down
                if c+1 < len(grid[0]):
                    stack.append((r, c+1)) # up

                print(count)

            print("AREA", area, "count", count)  
            area = max(area, count)
            
            
            return area 

 

        for r in range(rows):
            for c in range(cols): 
                if grid[r][c] == 1:
                    area = max(area, dfs(r,c))

        return area


        