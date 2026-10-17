class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use a min heap of size k storing k maximums 
        minheap = []
        for n in nums:
            if len(minheap) < k:
                heapq.heappush(minheap, n)
            elif minheap[0] < n:
                heapq.heappop(minheap)
                heapq.heappush(minheap, n)

        return minheap[0]
