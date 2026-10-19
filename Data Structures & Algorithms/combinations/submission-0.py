class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        candidate = []
        def backtrack(start: int):
            if len(candidate) == k:
                res.append(candidate[:])
                return
            
            for i in range(start, n+1):
                candidate.append(i)
                backtrack(i+1)
                candidate.pop()
            return 
        
        backtrack(1)
        return res

        # backtrack(2, 3)
        # backtrack(3, 1)
        # candidate = [2, ]
        # res = [[1, 2, 3]]
        




            
            