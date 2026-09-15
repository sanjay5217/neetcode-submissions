class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for i in range(len(nums)):
            result = target - nums[i]
            if result in hashmap and hashmap[result] != i:
                return [i, hashmap[result]]