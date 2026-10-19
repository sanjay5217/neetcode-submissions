class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidate = []
        candidates.sort()

        def backtrack(start: int, current_sum: int) -> None:
            # Termination State
            # if we exceed the target sum, either its equal (append candidate)
            # or do nothing and return 
            if current_sum >= target:
                if current_sum == target:
                    res.append(candidate[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # Include choice
                # this means we add to candidate and populate current_sum
                candidate.append(candidates[i])
                current_sum += candidates[i]
                # backtrack the current state
                backtrack(i+1, current_sum)
                # Undo the choice
                # this means we remove the choice from candidate and decrement current_sum
                candidate.pop()
                current_sum -= candidates[i]
        
        backtrack(0, 0)
        return res

    # Trace candidates = [9,2,2,4,6,1,5], target = 8
    # res = [[2, 2, 4], [2, 6], [2,1,5]]
    # candidate = []
    # current_sum = 0
