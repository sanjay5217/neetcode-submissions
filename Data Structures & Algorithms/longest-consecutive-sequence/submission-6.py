class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        res = 0

        for n in numbers:
            if (n - 1) not in numbers:
                length = 1
                while (n + length) in numbers:
                    length += 1
                res = max(res, length)
        return res