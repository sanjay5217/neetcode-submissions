class Solution:
    def isValid(self, s: str) -> bool:
        par_map = {'(':')', '[':']', '{':'}'}
        stack = []

        for index in range(len(s)):
            if s[index] in par_map.keys():
                stack.append(s[index])
            elif s[index] in par_map.values():
                if not stack:
                    return False
                pair = stack.pop()
                if par_map[pair] != s[index]:
                    return False 
        if stack:
            return False
        return True