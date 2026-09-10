class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        result = 0
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if i == "+":
                    result = num1 + num2
                elif i == "-":
                    result = num1-num2
                elif i == "*":
                    result = num1*num2
                elif i == "/":
                    result = int(num1/num2)
                stack.append(result)
        return stack[-1]