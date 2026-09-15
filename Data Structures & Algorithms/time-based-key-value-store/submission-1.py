class TimeMap:

    def __init__(self):
        self._hashtable = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._hashtable[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        search_list = self._hashtable[key]
        print(search_list)
        left, right = 0, len(search_list) - 1
        ans = ""

        while left <= right:
            middle = (left + right) // 2
            if search_list[middle][1] <= timestamp:
                ans = search_list[middle][0]
                left = middle + 1

            else:
                right = middle - 1

        return ans


