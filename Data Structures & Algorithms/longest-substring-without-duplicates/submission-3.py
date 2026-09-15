class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        i = j = 0
        unique_chars = defaultdict(int)
        max_window = 0

        while j < len(s):
            unique_chars[s[j]] +=1

            if unique_chars[s[j]] > 1:
                max_window = max(max_window, j - i)
                while unique_chars[s[j]] > 1:
                    unique_chars[s[i]] -= 1
                    i+=1
            
            j+= 1
        
        return max(max_window, j - i)
