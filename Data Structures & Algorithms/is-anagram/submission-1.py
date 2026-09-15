class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_val = sorted([ord(char) for char in s])
        t_val = sorted([ord(char) for char in t])

        if len(s_val) != len(t_val): 
            return False

        for i in range(len(s_val)):
            if s_val[i] != t_val[i]:
                return False

        return True