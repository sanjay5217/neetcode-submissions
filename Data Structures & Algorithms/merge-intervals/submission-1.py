class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = intervals[:]
        sorted_intervals.sort(key=lambda x: x[0])
        res = [sorted_intervals[0]]

        for i in range(1, len(sorted_intervals)):
            start, end = sorted_intervals[i]
            last_start, last_end = res[-1]

            if start <= last_end:
                res.pop()
                res.append([min(start, last_start), max(end, last_end)])
            else:
                res.append(sorted_intervals[i])
        
        return res
                