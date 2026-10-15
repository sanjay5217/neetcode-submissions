class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # construct dp[i][j] grid with dimensions len(s1) + 1 and len(s2) + 1
        # j is the index at s1
        # i is the index at s2
        # we use 2d dp and build the grid bottom up with base cases i = 0 or j = 0. 

        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s1)+1) for _ in range(len(s2)+1)]
        dp[0][0] = True 

        for i in range(len(s2)+1):
            for j in range(len(s1)+1):
                if i==0 and j==0:
                    continue
                if j==0:
                    dp[i][j] = dp[i-1][j] and s2[i-1] == s3[j+i-1]
                elif i==0:
                    dp[i][j] = dp[i][j-1] and s1[j-1] == s3[j+i-1]
                else:
                    dp[i][j] = (
                        (dp[i][j-1] and s1[j-1] == s3[j+i-1]) or \
                        (dp[i-1][j] and s2[i-1] == s3[j+i-1])
                    )
                
        return dp[-1][-1]


