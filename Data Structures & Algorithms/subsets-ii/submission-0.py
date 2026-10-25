class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        candidate = []

        def backtrack(i: int) -> None:
            if i == len(nums):
                res.append(candidate[:])
                return 
            
            candidate.append(nums[i])
            backtrack(i+1)
            candidate.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1)
        
        backtrack(0)
        return res

