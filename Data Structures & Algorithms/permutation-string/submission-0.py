class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Construct frequency dictionary of s1
        freq_s1 = [0] * 26
        for char in s1:
            freq_s1[ord(char) - ord('a')] += 1
        
        left = right = 0
        freq_s2 = [0] * 26
        while right < len(s2):
            freq_s2[ord(s2[right]) - ord('a')] += 1

            if right - left + 1 == len(s1):
                if freq_s2 == freq_s1: # O(1) comparison
                    return True
                else:
                    freq_s2[ord(s2[left]) - ord('a')] -= 1
                    left += 1
            
            right += 1
        
        return False
