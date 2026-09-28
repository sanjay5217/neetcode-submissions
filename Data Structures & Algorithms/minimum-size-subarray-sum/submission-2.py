class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sum of subarray >= target
        # return the minimum length of the subarray that qualifies the condition

        # Brute-force Approach: 
        # Find all subarrays and check if sum >= target and track the minimum length
        # Time complexity: 
        # Getting all subarrays is O(n^2) and the 
        # sum operation is O(n), resulting in O(n^3)

        # Proposed Approach:
        # Maintain a sliding window with its sum tracked

        left = current_sum = 0
        res = float("inf")
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                res = min(res, right - left + 1)
                current_sum -= nums[left]
                left += 1

        if res == float("inf"):
            return 0
        return res

        # Trace: target = 10, nums = [2,1,5,1,5,3]
        # left = 3
        # right = 5
        # current_sum = 9
        # res = 3
