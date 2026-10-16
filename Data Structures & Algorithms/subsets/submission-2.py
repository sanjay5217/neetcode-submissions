class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        candidate = []

        def dfs(index: int) -> None:
            # termination state 
            if index >= len(nums):
                # making this copy is O(len(candidate))
                res.append(candidate[:])
                return 
            # include nums[index]
            candidate.append(nums[index])
            dfs(index+1)
            # no exlcude nums[index]
            candidate.pop()
            dfs(index+1)
        
        # time complexity: theres a total of 2^n calls 
        # for the dfs so O(n x 2^n) including making the copy of the list

        # space complexity: we have candidates which is at most n items so O(n)
        # we do not count the answer space complexity, but that would be O(2^n)
        
        dfs(0)
        return res