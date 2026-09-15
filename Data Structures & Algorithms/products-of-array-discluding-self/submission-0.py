class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix AND suffix 
        prefix, postfix = 1, 1
        res = []

        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]

        for j in range(len(nums)-1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        
        return res

        