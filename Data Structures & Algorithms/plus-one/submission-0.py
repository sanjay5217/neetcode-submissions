class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = [0] + digits[:]
        addOne = True

        for i in range(len(res) - 1, -1, -1):
            if addOne:
                res[i] += 1
            if res[i] == 10:
                addOne = True
                res[i] = 0
            else:
                addOne = False
                break
        
        if res[0] == 0:
            return res[1:]
        elif res[0] == 10:
            return [1, 0] + res[1:]
        return res