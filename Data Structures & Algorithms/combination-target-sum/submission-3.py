class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        candidate = []

        def backtrack(start: int, current_sum: int) -> None:
            # Termination state
            if current_sum >= target:
                if current_sum == target:
                    res.append(candidate[:])
                return
            
            # Pick our choice
            for i in range(start, len(nums)):
                if current_sum + nums[i] > target:
                    continue
                candidate.append(nums[i])
                # dfs on other possible choices
                backtrack(i, current_sum + nums[i])
                # Undo our choice
                candidate.pop()
        
        backtrack(0, 0)
        return res

    # Dry Run
    # nums = [2, 5, 6, 9], target = 9
    # res = [[2, 2, 5], [9]]
    # candidate = [9]
    # current_sum = 9
