class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking algorithm

        # for the current number, we essentially append it to 
        # the permutations of the leftovers

        res = []
        used = set()

        def dfs(nums: list[int], candidate: list[int]) -> None:
            # termination condition is when candidate has all options which means
            # it matches the length of the option sapce 
            if len(candidate) == len(nums):
                res.append(candidate[:])
                return 

            for n in nums:
                if n not in used:
                    # we pick an option not in used
                    candidate.append(n)
                    used.add(n)
                    # now we need to explore further options 
                    # that branch of our current option
                    dfs(nums, candidate)

                    # now we remove our current option
                    # recursively we will explore other options on this level now
                    candidate.pop()
                    used.remove(n)
        
        dfs(nums, [])
        return res



