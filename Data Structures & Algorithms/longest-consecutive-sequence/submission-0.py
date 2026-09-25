class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hash_table = {2: 0, 20: 0, 4: 1, 10: 0, 3: 1, 5: 1}
        # 1 if n-1 exists and 0 otherwise
        # 2 -> 3 -> 4 -> 5 
        # 20 
        # 10
        # return 4

        # nums = [2,20,4,10,3,4,5]
        # hash_table = {2: 0, 20: 0, 4: 1, 10: 0, 3: 1, 5: 1}

        hash_table = defaultdict(int)
        for n in nums:
            if n not in hash_table:
                hash_table[n] = 0
            if n-1 in hash_table:
                hash_table[n] = 1
            if n + 1 in hash_table:
                hash_table[n+1] = 1
        res = 0
        # iterate through the table where the values are 0 (start of potential paths)

        # curr = 6
        # path_length = 4
        for path in hash_table.keys():
            if hash_table[path] == 0:
                curr = path
                path_length = 0
                while curr in hash_table:
                    path_length += 1
                    curr += 1
                res = max(res, path_length)
        return res