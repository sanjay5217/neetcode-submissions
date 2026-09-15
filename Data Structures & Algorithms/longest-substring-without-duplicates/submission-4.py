class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set()
        i = j = 0
        max_window = 0

        while j < len(s):
            while s[j] in unique_chars:
                unique_chars.remove(s[i])
                i+=1
            
            unique_chars.add(s[j])
            max_window = max(max_window, j - i + 1)
            j+=1
        
        return max_window
