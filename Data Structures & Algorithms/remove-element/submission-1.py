class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0

        while index < len(nums):
            if nums[index] != val:
                index += 1
            else:
                nums.pop(index)
        
        return len(nums)