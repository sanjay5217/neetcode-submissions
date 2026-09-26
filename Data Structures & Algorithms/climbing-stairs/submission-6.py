class Solution:
    def climbStairs(self, n: int) -> int:
        # optimized (only need last 2 elements)
        if n <= 2:
            return n
        # recurrance relation: C(n) = C(n-1) + C(n-2)
        one_step, two_step = 2, 1
        for i in range(3, n + 1):
            current = one_step + two_step
            two_step = one_step
            one_step = current
        return one_step