class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if stack != [] and stack[-1][0] < temperatures[i]:
                while stack != [] and stack[-1][0] < temperatures[i]:
                    temp = stack.pop()
                    output[temp[1]]= i - temp[1]
            
            stack.append((temperatures[i], i))

        return output