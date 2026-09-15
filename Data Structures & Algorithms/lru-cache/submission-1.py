class DNode:
    key: Optional[int]
    value: Optional[int]
    next: Optional[DNode]
    prev: Optional[DNode]

    def __init__(self, key: Optional[int], value: Optional[int]) -> None:
        self.key, self.value = key, value
        self.next, self.prev = None, None

class LRUCache:
    capacity: int
    cache: dict[int, DNode]
    head: DNode
    tail: DNode
    
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}
        self.head = DNode(None, None)
        self.tail = DNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, node: DNode) -> None:
        after = self.head.next
        self.head.next, node.next = node, after
        after.prev, node.prev = node, self.head

    def pop(self, node: DNode) -> None:
        before, after = node.prev, node.next
        before.next, after.prev = after, before

    def get(self, key: int) -> int:
        if key in self.cache:
            self.pop(self.cache[key])
            self.append(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.pop(self.cache[key])
        self.cache[key] = DNode(key, value)
        self.append(self.cache[key])

        if len(self.cache) > self.capacity:
            node = self.tail.prev
            self.pop(node)
            del self.cache[node.key]
        
