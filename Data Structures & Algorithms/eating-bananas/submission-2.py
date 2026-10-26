class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            rate = (left + right) // 2
            count = 0
            for bananas in piles:
                count += math.ceil(bananas/rate)
            if count > h:
                left = rate+1
            else:
                res = rate
                right = rate-1
        
        return res
            
