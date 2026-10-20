class Solution:
    def is_palindrome(self, s: string, left: int, right: int) -> bool:
        while left <= right:
            if s[left] != s[right]:
                return False 
            left += 1
            right -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        # Example case: s = "abcba" length is 5
        # ["a", "b", "c", "b", "a"]
        # ["a", "bcb", "a"]
        # ["abcba"]

        res = []
        candidate = []

        def backtrack(i: int) -> None:
            if i >= len(s):
                res.append(candidate[:])
                return 
        
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    candidate.append(s[i:j+1])
                    backtrack(j+1)
                    candidate.pop()
            

        backtrack(0)
        return res 






