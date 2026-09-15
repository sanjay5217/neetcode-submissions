class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        stack = []
        count = 0

        for p, s in cars:
            stack.append((target-p) / s)
            count+=1
            if count > 1 and stack[-1] <= stack[-2]:
                stack.pop()
                count-=1
        
        return count