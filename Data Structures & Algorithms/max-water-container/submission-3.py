class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_area = 0

        while i < j:
            max_area = max(max_area, min(heights[i], heights[j]) * (j - i))
            
            if heights[j] > heights[i]:
                i+=1
            else:
                j-=1
        
        return max_area