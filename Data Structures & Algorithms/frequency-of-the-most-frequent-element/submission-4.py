class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1
        # sort the array 
        sorted_nums = sorted(nums)
        left = 0

        # value at right pointer is frequent element
        # maintain the sum within the window
        # we check if length of window x value at right pointer 
        # < total sum of window + k
        window_sum = sorted_nums[0]
        res = 1
        for right in range(1, len(sorted_nums)):
            window_sum += sorted_nums[right]

            while (right - left + 1) * sorted_nums[right] > window_sum + k:
                window_sum -= sorted_nums[left]
                left += 1
            res = max(res, right - left + 1)
        
        return res

