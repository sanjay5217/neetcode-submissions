class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]

        all_sets = []
        current_subset = self.subsets(nums[1:])
        for subset in current_subset:
            curr = subset + [nums[0]]
            all_sets.append(curr)
        all_sets.extend(current_subset)
        return all_sets


