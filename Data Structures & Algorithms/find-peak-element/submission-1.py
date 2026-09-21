class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if mid > 0:
                left_neighbor = nums[mid-1]
            else:
                left_neighbor = float("-inf")
            if mid < len(nums) - 1:
                right_neighbor = nums[mid+1]
            else:
                right_neighbor = float("-inf")
            
            if left_neighbor < nums[mid] and nums[mid] > right_neighbor:
                return mid
            elif left_neighbor < nums[mid] and nums[mid] < right_neighbor:
                left = mid + 1
            elif left_neighbor > nums[mid] and nums[mid] > right_neighbor:
                right = mid - 1
            else:
                if left_neighbor > right_neighbor:
                    right = mid - 1
                else:
                    left = mid + 1