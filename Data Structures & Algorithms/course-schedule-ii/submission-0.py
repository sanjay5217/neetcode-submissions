class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {node: [] for node in range(numCourses)}
        for neighbor, node in prerequisites:
            graph[node].append(neighbor)

        # Initialize indegree
        indegree = {node: 0 for node in range(numCourses)}
        for node in graph.keys():
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        
        # Enqueue indegrees of 0s
        queue = deque()
        for node in indegree.keys():
            if indegree[node] == 0: queue.append(node)
        order = []
        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

            order.append(node)
        
        if len(order) == numCourses:
            return order 
        return []





        






        