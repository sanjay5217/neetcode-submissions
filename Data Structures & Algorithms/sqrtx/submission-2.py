class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left, right = 1, x
        ans = 0

        while left <= right:
            middle = (left + right) // 2

            if middle * middle == x:
                return middle

            elif middle * middle < x:
                ans = middle
                left = middle + 1
            
            else:
                right = middle - 1

        return ans
