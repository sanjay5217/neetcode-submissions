class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom-up approach
        if n <= 2:
            return n
        # recurrance relation: C(n) = C(n-1) + C(n-2)
        dp = [0] * (n+1) # n + 1 space since we want dp[n] = C(n)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]