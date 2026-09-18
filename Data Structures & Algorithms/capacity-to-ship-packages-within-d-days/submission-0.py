class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = right

        def checkCapacity(capacity: int) -> int:
            # Returns the days it takes to unload
            days = 1
            current_load = 0
            for load in weights:
                if current_load + load > capacity:
                    current_load = 0
                    days += 1
                current_load += load
            
            return days
        
        # capacity: 8,  weights: [1, 5, 4, 4, 2, 3]
        # days = 2
        # current_load = 4
        # load = 4

        while left <= right:
            capacity = (left + right) // 2
            if checkCapacity(capacity) <= days:
                res = min(capacity, res)
                right = capacity - 1
            else:
                left = capacity + 1
        return res
            



