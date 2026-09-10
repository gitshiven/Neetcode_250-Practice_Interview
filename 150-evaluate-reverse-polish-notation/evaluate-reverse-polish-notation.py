class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        result = 0
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
                
            elif i == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                result = num1 + num2
                stack.append(result)
            elif i == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                result = num2-num1
                stack.append(result)
            elif i == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                result = num2 * num1
                stack.append(result)
            elif i == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                result = int(num2 / num1)
                stack.append(result)
        return stack[0]
            
            
            