class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 1, 2, 8]
        # right = 48
        # [48, 24, 12, 8]

        # [-1, 0, 1, 2, 3]
        # [0, -6, 0, 0, 0]
        # right = 0
        res = [0] * len(nums)
        res[0] = 1
        
        for i in range(1, len(nums)):
            res[i] = nums[i-1] * res[i-1]
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        
        return res

