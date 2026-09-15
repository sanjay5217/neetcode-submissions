class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = [] #stack
        choices = ["+", "-", "*", "/"]
        current = 0

        for item in tokens:
            if item not in choices:
                numbers.append(int(item))
            else:
                n1, n2 = numbers.pop(), numbers.pop()
                if item == "+": current = n1 + n2
                elif item == "-": current = n2 - n1
                elif item == "*": current = n1 * n2
                else: current = int(n2 / n1) 
                numbers.append(current)
        
        return numbers[0]
