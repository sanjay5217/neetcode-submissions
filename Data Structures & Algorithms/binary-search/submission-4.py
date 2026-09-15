class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        if not nums:
            return -1

        elif len(nums) == 1:
            if nums[0] == target: return 0
            else: return -1

        else:
            mid = len(nums) // 2
            add = 0
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                index = self.search(nums[mid:], target)
                add = mid
            else:
                index = self.search(nums[:mid], target)
            
            if index != -1:
                return index + add
            else:
                return -1
        