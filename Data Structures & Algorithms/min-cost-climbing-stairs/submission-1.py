class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # starting at index 0 = cost[0] + min(minCost(cost[1:]), minCost(cost[2:]))
        # starting at index 1 = cost[1] + min(minCost(cost[2:]), minCost(const[3:]))

        def minCost(cost: list[int], memo: dict[int, int], i: int) -> int:
            if i >= len(cost):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(minCost(cost, memo, i + 1),
                                     minCost(cost, memo, i + 2))
            return memo[i]
        
        memo = {}
        return min(minCost(cost, memo, 0), minCost(cost, memo, 1))

    # cost = [1, 2, 1, 2, 1, 1, 1]
    # memo = {6: 1, 5: 1, 4: 2, 3: 3, 2: 3, 1: 5}
    # minCost(0) = 1 + min(5, 3) = 1 + 3 = 4
    # minCost(1) = 2 + min(3, 3) = 2 + 3 = 5
    # minCost(2) = 1 + min(2, 3) = 1 + 2 = 3
    # minCost(3) = 2 + min(2, 1) = 2 + 1 = 3
    # minCost(4) = 1 + min(1, 1) = 2
    # minCost(5) = min(1, 1) = 1
    # minCost(6) = min(1, 1) = 1