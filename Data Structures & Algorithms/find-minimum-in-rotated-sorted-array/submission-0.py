class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right - 1:
            middle = (left + right) // 2
            if nums[middle] < nums[right]:
                right = middle
            elif nums[middle] > nums[left]:
                left = middle
        
        return min(nums[left], nums[right])
        

