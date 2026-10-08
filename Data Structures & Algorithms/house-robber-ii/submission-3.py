class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def house_rob(houses: list[int]) -> int:
            if len(houses) == 1:
                return houses[0]
            
            a_houses, p_houses = max(houses[0], houses[1]), houses[0]
            res = a_houses
            for i in range(2, len(houses)):
                res = max(a_houses, houses[i] + p_houses)
                p_houses = a_houses
                a_houses = res 
            return res 

        return max(house_rob(nums[:len(nums)-1]), house_rob(nums[1:]))