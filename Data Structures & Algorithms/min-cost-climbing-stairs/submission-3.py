class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:        
        memo = {}

        def minCost(i: int) -> int:
            if i >= len(cost):
                return float('inf')
            
            if i == len(cost) - 1 or i == len(cost) - 2:
                memo[i] = cost[i]
                return memo[i]
            
            if i not in memo:
                memo[i] = cost[i] + min(minCost(i+1), minCost(i+2))       
            return memo[i]
        
        return min(minCost(0), minCost(1))