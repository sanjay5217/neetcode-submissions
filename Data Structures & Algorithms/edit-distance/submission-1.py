class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #   m o n e y
        # m 0 1 2 3 4
        # o 1 0 1 2 3
        # n 2 1 0 1 2
        # k 3 2 1 1 2
        # y 4 3 2 2 1
        # s 5 4 3 3 2

        # recurrance relation
        # if word1[i] == word2[j], then dp[i][j] = dp[i-1][j-1]
        # otherwise dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]

        for i in range(len(word1)+1):
            dp[i][0] = i
        
        for j in range(len(word2)+1):
            dp[0][j] = j
    
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
        return dp[-1][-1]



        