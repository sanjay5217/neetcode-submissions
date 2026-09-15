class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_max = curr_min = 1
        
        for element in nums:
            temp = curr_max * element
            curr_max = max(element, curr_max * element, curr_min * element)
            curr_min = min(element, temp, curr_min * element)
            res = max(res, curr_max)

        return res
            

