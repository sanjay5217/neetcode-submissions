class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []

        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            k = 0 - sorted_nums[i]
            remain = self.twoSum(sorted_nums, i+1, k, sorted_nums[i])
            if remain:
                res.extend(remain)

        return res
    
    
    def twoSum(self, nums: List[int], start: int, k: int, addition: int) -> List[List[int]]:
        res = []
        left, right = start, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < k:
                left += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                res.append([addition, nums[left], nums[right]])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

        return res



        

