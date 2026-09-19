class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(math.sqrt((p[0] ** 2) + (p[1] **2)), p) for p in points]
        heapq.heapify(distances)
        res = []
        for _ in range(k):
            min_dist = heapq.heappop(distances)
            res.append(min_dist[1])
        return res

    # points = [[0,2],[2,0],[2,2]], k = 2
    # distances = [(2, [0, 2]), (2, [2, 0]), (2.82.., [2,2])]
    # res = [[0, 2], [2, 0]]