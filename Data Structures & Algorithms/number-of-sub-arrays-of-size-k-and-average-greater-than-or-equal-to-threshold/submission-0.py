class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = right = 0
        current_sum = 0
        count = 0

        while right < len(arr):
            current_sum += arr[right]
            if right - left + 1 == k:
                if current_sum / k >= threshold:
                    count += 1
                current_sum -= arr[left]
                left += 1

            right += 1

        return count
