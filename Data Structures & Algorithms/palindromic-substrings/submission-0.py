class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        res = 0
        for j in range(len(s)):
            for i in range(len(s)):
                if i <= j:
                    dp[i][j] = s[i] == s[j] and (j-i < 2 or dp[i+1][j-1])
                    if dp[i][j]:
                        res += 1
                else:
                    break 
        return res

        #j    0 1 2
        #     a b c
        # 0 a T F F
        # 1 b F T F
        # 2 c F F T
                