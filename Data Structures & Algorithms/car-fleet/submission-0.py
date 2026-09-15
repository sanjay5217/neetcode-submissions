class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        stack = []
        count = 0

        for car in cars:
            if not stack:
                stack.append(car)
                count+=1
            else:
                time = (target - car[0]) / car[1]
                last_time = (target - stack[-1][0]) / stack[-1][1]
                if time > last_time:
                    stack.append(car)
                    count+=1
        
        return count