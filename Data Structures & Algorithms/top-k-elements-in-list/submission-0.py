class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        collections = defaultdict(int)

        for number in nums:
            collections[number] += 1
        
        max_heap = [(-1 * count, item) for item, count in collections.items()]
        heapq.heapify(max_heap)
        output = []

        for _ in range(k): output.append(heapq.heappop(max_heap)[1])
        return output
