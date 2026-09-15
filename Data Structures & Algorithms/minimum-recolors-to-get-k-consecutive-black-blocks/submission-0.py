class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = right = 0
        count = 0
        min_count = float('inf')

        while right < len(blocks):
            if blocks[right] == "W":
                count+=1
                
            if right - left + 1 == k:
                min_count = min(min_count, count)
                
                if blocks[left] == "W":
                    count -= 1
                
                left += 1
            
            right+=1
        
        return min_count