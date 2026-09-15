class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        curr, index = nums[0], 1

        while index < len(nums):
            if curr == nums[index]:
                nums.pop(index)
            else:
                curr = nums[index]
                index += 1
        
        return len(nums)
        
