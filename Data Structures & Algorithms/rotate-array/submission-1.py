class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverse(start: int, end: int) -> None:
            i, j = start, end 
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
        
        index = k % len(nums)
        reverse(0, len(nums) - 1)
        reverse(0, index-1)
        reverse(index, len(nums) - 1)


        