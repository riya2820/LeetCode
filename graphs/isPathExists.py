class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        for k, v in edges:
            adj_list[k].append(v)
            adj_list[v].append(k)
        visited = set()
        
        def dfs(node):
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                for edge in adj_list[node]:
                    res = dfs(edge)
                    if res: return True
        return dfs(source)
