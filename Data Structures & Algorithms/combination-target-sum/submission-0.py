class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums = [2, 5, 6, 1, 4] target = 6
        # first decision: include 2
            # sum: 2, cand = [2]
            # include 2
                # sum: 4, cand = [2, 2]
                    # include 2
                        # sum: 6, cand = [2, 2, 2] -> terminate because sum=target
                    # include 1 (twice)
                        # sum: 6, cand = [2, 2, 1, 1] -> terminate
            # we include 5, 6 and they turn out to be sum < 0 so we stop
            # include 1 will give us [2, 1, 1, 1, 1]
            # include 4
                # sum: 6, cand = [2, 4] -> terminate because sum>=target
        # include 5
            # sum: 5, cand = [5]
            # include 5, 6 will have sum>=target
            # include 1
                # sum: 6, cand = [5, 1] -> terminate because sum=target
        # include 6
            # sum: 6, cand = [6] -> terminate 
        # include 1
            # sum: 1, cand = [1]
                # include 1 (this will go for 6 times)
                # ... sm: 6, cand = [1, 1, 1, 1, 1, 1]
                # we will backtrack to cand [1, 1]
                # only other option is now 4 so we have [1, 1, 4]
        
        res = []
        candidate = []
        def dfs(index: int, current_sum: int) -> None:
            # termination state (base case)
            if current_sum >= target:
                if current_sum == target:
                    res.append(candidate[:])
                return
            for i in range(index, len(nums)):
                # include current choice
                candidate.append(nums[i])
                current_sum += nums[i]
                dfs(i, current_sum)
                # exclude current choice
                candidate.pop()
                current_sum -= nums[i]
        
        dfs(0, 0)
        return res

        # Trace 
        # [2, 4, 6] target = 6
        # res = [[2, 2, 2], ]
        # candidate = [2, 2]
        # current_sum = 4
        # choices = [4, 6]
        # dfs(0)
        # dfs(0)
        # dfs(0)


            

                    
                    

        
        

        
