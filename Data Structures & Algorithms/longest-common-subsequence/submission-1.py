class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # recurrance relation:
        # dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        # if text1[j] == text2[i], then another comparison
        # dp[i][j] = max(dp[i][j], 1 + dp[i-1][j-1])

        # initialize dp grid 
        WORD_ONE, WORD_TWO = len(text1)+1, len(text2)+1
        dp = [[0] * WORD_ONE for _ in range(WORD_TWO)]

        # indexing by 1 makes edge case handling wayyyy easier. 
        for i in range(1,WORD_TWO):
            for j in range(1,WORD_ONE):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = max(dp[i][j], 1 + dp[i-1][j-1])
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        return dp[-1][-1]

        # Trace 
        # text1 = crabt, text2 = cat
        # dp = [ [1, 0, 0, 0, 0] 
        #        [0, 0, 0, 0, 0]
        #        [0, 0, 0, 0, 0] ]

        # i = 0
        # j = 0
        # dp[i][j] = 

