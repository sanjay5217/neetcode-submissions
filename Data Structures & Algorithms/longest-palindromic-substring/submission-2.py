class Solution:
    def longestPalindrome(self, s: str) -> str:
        #     b a b a d
        #     0 1 2 3 4 
        # b 0 T F T F F
        # a 1   T F F F
        # b 2     T F F
        # a 3       T F
        # d 4         T

        #     a a a 
        #     0 1 2
        # a 0 T T T
        # a 1   T T
        # a 2     T
        
        # order of populating: start at col 1, iterate through all rows, then move on to col 2

        # length = j-i+1
        # dp[i][j] = s[i] == s[j] and (j-i+1 < 2 or dp[i+1][j-1])

        dp = [[False] * (len(s)) for _ in range(len(s))]
        res = ""

        for j in range(len(s)):
            for i in range(len(s)):
                if i <= j:
                    dp[i][j] = s[i] == s[j] and (j-i < 2 or dp[i+1][j-1])
                    if dp[i][j] and len(res) < j-i+1:
                        res = s[i:j+1]
                else:
                    break 
        return res
