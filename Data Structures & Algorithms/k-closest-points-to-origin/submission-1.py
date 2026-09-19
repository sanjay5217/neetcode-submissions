class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Better Approach: Maintain size k Max heap
        # Time Complexity: O(n log (k)) 
        # Space Complexity: O(k)
        distances = []
        for p in points:
            dist = -1 * math.sqrt((p[0] ** 2) + (p[1] **2))
            heapq.heappush(distances, (dist, p))
            if len(distances) > k:
                heapq.heappop(distances)

        res = []
        while distances:
            min_dist = heapq.heappop(distances)
            res.append(min_dist[1])
        return res