class DynamicArray:
    capacity: int
    size: int
    _array: list

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self._array = [None] * capacity

    def get(self, i: int) -> int: return self._array[i]

    def set(self, i: int, n: int) -> None: self._array[i] = n

    def pushback(self, n: int) -> None:
        if self.size >= self.capacity:
            self.resize()
        self._array[self.size] = n
        self.size+=1

    def popback(self) -> int:
        self.size -= 1
        element = self._array[self.size]
        self._array[self.size] = None
        return element

    def resize(self) -> None:
        self.capacity*=2
        new_array = [None] * self.capacity

        for i in range(self.size):
            new_array[i] = self._array[i]

        self._array = new_array

    def getSize(self) -> int: return self.size

    def getCapacity(self) -> int: return self.capacity
