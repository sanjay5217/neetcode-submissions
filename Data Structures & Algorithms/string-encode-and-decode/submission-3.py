class Solution:

    def encode(self, strs: List[str]) -> str:
        main = ""
        for string in strs:
            main += str(len(string)) + "#" + string
        
        return main

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            output.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return output