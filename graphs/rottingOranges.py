from collections import deque
    # (1,1) fill 2
    # 2 1 1     2 2 1    2 2 2    2 2 2    2 2 2
    # 1 1 0 ->  2 1 0 -> 2 2 0 -> 2 2 2 -> 2 2 0
    # 0 1 1     2 1 1    2 1 1    2 2 1    2 2 2
'''
    queue = deque([node])
    seen.add(node)
    while queue:
        curr = queue.popleft()
        for neighbor in curr.neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor) 
'''

def rottingOranges(grid):
    if not grid or not grid[0]:
        return

    rows, cols = len(grid), len(grid[0])
    mins = 0
    fresh = 0
    seen = set()
    q = deque()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))
                seen.add((r, c))
            elif grid[r][c] == 1:
                fresh += 1
        
    if fresh == 0:
        return 0


    while q and fresh > 0:
        for _ in range(len(q)):
            r,c = q.popleft() # 0, 0
            if grid[r][c] == 0:
                continue

            if r > 0 and grid[r-1][c] == 1: # left
                if (r-1,c) not in seen:
                    seen.add((r-1,c))
                    q.append((r-1,c))
                    grid[r-1][c] = 2
                    fresh -= 1

            if r+1 < len(grid) and grid[r+1][c] == 1: # right
                if (r+1,c) not in seen:
                    seen.add((r+1,c))
                    q.append((r+1,c))
                    grid[r+1][c] = 2
                    fresh -= 1

            if c > 0 and grid[r][c-1] == 1: # down
                if (r,c-1) not in seen:
                    seen.add((r,c-1))
                    q.append((r,c-1))
                    grid[r][c-1] = 2
                    fresh -= 1

            if c+1 < len(grid[0]) and grid[r][c+1] == 1: # up
                if (r,c+1) not in seen: 
                    seen.add((r,c+1))
                    q.append((r,c+1))
                    grid[r][c+1] = 2
                    fresh -= 1
        
        mins += 1

    if fresh == 0:
        return mins

    return -1



# A = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(rottingOranges(grid))
