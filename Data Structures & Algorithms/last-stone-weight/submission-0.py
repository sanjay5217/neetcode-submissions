class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        heap = [(-1 * weight) for weight in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            weight_1 = -1 * heapq.heappop(heap)
            weight_2 = -1 * heapq.heappop(heap)
            remaining = weight_1 - weight_2
            if remaining > 0:
                heapq.heappush(heap, -1 * remaining)

        if heap:
            return -1 * heap[0]
        else:
            return 0

    # Trace 
    # stones = [2,2]
    # heap = [-1]
    # weight_1 = 2
    # weight_2 = 2
    # remaining = 0