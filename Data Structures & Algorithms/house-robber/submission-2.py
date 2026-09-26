class Solution:
    def rob(self, nums: List[int]) -> int:
        # [1, 3, 1, 1, 9]
        # 12

        # [2, 9, 8, 3, 6]
        # hr(0) = 2
        # hr(1) = 9
        # hr(2) = max(hr(1), 8 + hr(0)) = max(9, 8 + 2) = 10
        # hr(3) = max(hr(2), 3 + hr(1)) = max(10, 3 + 9) = 12
        # hr(4) = max(hr(3), 6 + hr(2)) = max(12, 6 + 10) = 10

        # reccurance relation = hr(n) = max(hr(n-1), nums[n] + hr(n-2))

        # Tabulation (Bottom-Up Approach)
        if len(nums) == 1:
            return nums[0]
        
        adjacent_houses, previous_houses = max(nums[1], nums[0]), nums[0]
        res = adjacent_houses
        for i in range(2, len(nums)):
            res = max(adjacent_houses, nums[i] + previous_houses)
            previous_houses = adjacent_houses
            adjacent_houses = res
        
        return res
        


