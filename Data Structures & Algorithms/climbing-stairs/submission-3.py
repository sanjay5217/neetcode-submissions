class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.climbMemo(n, memo)

    
    def climbMemo(self, n: int, memo) -> int:
        if n in memo:
            return memo[n]
        if n <= 2:
            return n
        memo[n] = self.climbMemo(n-1, memo) + self.climbMemo(n-2, memo)
        return memo[n]