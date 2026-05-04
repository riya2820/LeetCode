from collections import deque

seen = set()

def dfs(node):
    stack = [node]
    while stack:
        curr = stack.pop()
        if curr in seen: 
            continue
        seen.add(curr)
        for neighbor in curr.neighbors:
            stack.append(neighbor)


seen = set()

def bfs(node):
    queue = deque([node])
    seen.add(node)
    while queue:
        curr = queue.popleft()
        for neighbor in curr.neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)