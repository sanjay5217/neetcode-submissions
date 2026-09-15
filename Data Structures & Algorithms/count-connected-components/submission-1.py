class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # construct graph
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        visited = set()
        
        def dfs(node: int):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        count = 0
        for node in graph.keys():
            if node not in visited:
                dfs(node)
                count += 1

        return count + (n - len(graph.keys()))
            

        