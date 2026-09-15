class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = defaultdict(lambda: float('inf'))
        dist[k] = 0
        p_queue = [(0, k)]
        max_dst = -1

        while p_queue:
            curr_dst, curr_node = heapq.heappop(p_queue)
            if curr_dst > dist[curr_node]:
                continue
            
            for edges in times:
                if edges[0] == curr_node:
                    new_dist = edges[2] + curr_dst
                    if new_dist < dist[edges[1]]:
                        dist[edges[1]] = new_dist
                        heapq.heappush(p_queue, (new_dist, edges[1]))
        
        if len(dist) != n:
            return -1
        else:
            return max(dist.values())
        


