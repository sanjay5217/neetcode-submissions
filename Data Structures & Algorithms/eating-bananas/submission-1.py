class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        rate = right

        while left <= right:
            middle = (left + right) // 2
            time_taken = 0

            for bananas in piles:
                time_taken += math.ceil(bananas / middle)
                
            if time_taken <= h:
                rate = middle
                right = middle - 1
                
            else:
                left = middle + 1
        
        return rate

