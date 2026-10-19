class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        if not digits:
            return []

        res = []
        candidate = ""

        def backtrack(start: int):
            nonlocal candidate
            # Termination State 
            if len(candidate) == len(digits):
                res.append(candidate[:])
                return

            digit = digits[start]
            choices = mapping[digit]
            for i in range(len(choices)):
                # pick our choice
                candidate += choices[i]
                # backtrack further with the next current_digit
                backtrack(start+1)
                # undo our choice
                candidate = candidate[:-1]

        backtrack(0)
        return res 
    
    # Dry run: "34"
    # res = ["dg", "dh", "di","eg","eh","ei","fg","fh","fi"]
    # candidate = "e"
    # choices = "def"
    #"3": "def", "4": "ghi"




