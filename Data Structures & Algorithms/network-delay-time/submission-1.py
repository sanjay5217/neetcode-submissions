class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = defaultdict(lambda: float('inf'))
        dist[k] = 0
        p_queue = [(0, k)]
        max_dst = -1


        graph = defaultdict(list)
        for edges in times:
            graph[edges[0]].append((edges[1], edges[2]))

        while p_queue:
            curr_dst, curr_node = heapq.heappop(p_queue)
            if curr_dst > dist[curr_node]:
                continue
            
            for neighbor, weight in graph[curr_node]:
                new_dist = weight + curr_dst
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(p_queue, (new_dist, neighbor))
        
        if len(dist) != n:
            return -1
        else:
            return max(dist.values())
