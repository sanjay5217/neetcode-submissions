class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Example Run
        # numCourses = 4
        # prerequisites = [[0, 1], [2, 1], [3, 2]]
        # return true because we can take 1 -> 0 -> 2 -> 3 or 1 -> 2 -> 0 -> 3

        # [0, 1] means 1 -> 0

        # Kahn's Algorithm (Top Sort)
        # Construct the graph 
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
        
        return len(order) == numCourses





        






        