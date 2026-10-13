class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # recurrance relation:
        # dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        # if text1[j] == text2[i], then another comparison
        # dp[i][j] = max(dp[i][j], 1 + dp[i-1][j-1])

        # initialize dp grid 
        WORD_ONE, WORD_TWO = len(text1), len(text2)
        dp = [[0] * WORD_ONE for _ in range(WORD_TWO)]

        for i in range(WORD_TWO):
            for j in range(WORD_ONE):
                if j > 0 and i > 0:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                    if text1[j] == text2[i]:
                        dp[i][j] = max(dp[i][j], 1 + dp[i-1][j-1])
                else:
                    if text1[j] == text2[i]:
                        dp[i][j] = 1
                    elif j > 0:
                        dp[i][j] = max(dp[i][j], dp[i][j-1])
                    else:
                        dp[i][j] = max(dp[i][j], dp[i-1][j])
        
        return dp[-1][-1]

        # Trace 
        # text1 = crabt, text2 = cat
        # dp = [ [1, 0, 0, 0, 0] 
        #        [0, 0, 0, 0, 0]
        #        [0, 0, 0, 0, 0] ]

        # i = 0
        # j = 0
        # dp[i][j] = 

