class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target == row[-1]:
                return True
            if target < row[-1]:
                return self.b_search(row, target)

        return False
    

    def b_search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target: 
                return True
            
            elif nums[mid] > target: 
                right = mid - 1
            
            else:
                left = mid + 1
        
        return False