class MinStack:

    def __init__(self) -> None:
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        if not self._min_stack:
            self._min_stack.append(val)
        else:
            if val <= self._min_stack[-1]:
                self._min_stack.append(val)
        
        self._stack.append(val)

    def pop(self) -> None:
        val = self._stack.pop()
         
        if val == self._min_stack[-1]:
            self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]
        
    def getMin(self) -> int:
        return self._min_stack[-1]
        
