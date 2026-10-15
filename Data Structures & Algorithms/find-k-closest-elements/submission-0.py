class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # [1, 3, 4, 5, 8], x = 6, k = 2
        # left = 2
        # right = 3
        # d_left = 2
        # d_right = 2

        left, right = 0, len(arr) - 1

        while right - left + 1 > k:
            distance_left = abs(arr[left] - x)
            distance_right = abs(arr[right] - x)
            if distance_left > distance_right:
                left += 1
            else:
                right -= 1
        
        return arr[left:right+1]
            