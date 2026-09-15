class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] == target: return True
            elif row[-1] > target: return self.binary_search(row, target)

        return False


    def binary_search(self, nums: list[int], target: int) -> bool:
        if len(nums) == 1:
            if nums[0] == target: return True 
            else: return False 
        
        else:
            mid = len(nums) // 2

            if nums[mid] == target:
                return True 
            
            elif nums[mid] < target:
                return self.binary_search(nums[mid:], target)

            else:
                return self.binary_search(nums[:mid], target)