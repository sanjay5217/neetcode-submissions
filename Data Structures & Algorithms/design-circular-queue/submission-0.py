class MyCircularQueue:
    size: int
    capacity: int
    _queue: list[int]
    front: int
    rear: int

    def __init__(self, k: int):
        self.size = k
        self.capacity = 0
        self._queue = k * [None]
        self.front, self.rear = None, None        

    def enQueue(self, value: int) -> bool:
        #[2, 2, 3]
        #[N, N, 2]
        if self.capacity == 0:
            self.front = self.rear = 0
            self.capacity += 1
            self._queue[0] = value
            return True 
        # [N, N, N] -> [3, N, N]
        elif self.capacity < self.size:
            self.rear = (self.rear + 1) % self.size
            self.capacity += 1
            self._queue[self.rear] = value
            return True
        return False

    def deQueue(self) -> bool:
        if self.capacity == 0:
            return False 
        self._queue[self.front] = None
        self.capacity-=1
        if self.front == self.size - 1:
            self.front = 0
        else:
            self.front+=1
        if self.capacity == 0:
            self.rear = self.front = None
        return True         

    def Front(self) -> int:
        if not self.isEmpty():
            return self._queue[self.front]
        return -1
        

    def Rear(self) -> int:
        if not self.isEmpty():
            return self._queue[self.rear]
        return -1
        

    def isEmpty(self) -> bool:
        return self.capacity == 0
        

    def isFull(self) -> bool:
        return self.capacity == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()