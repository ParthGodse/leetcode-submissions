class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char.isdigit()  or (char[0] == '-' and char[1:].isdigit()):
                stack.append(int(char))
                #print(stack[-1])
            else:
                num2 = stack.pop()
                #print(stack[-1])
                num1 = stack.pop()
                if char == '+':
                    stack.append(num1 + num2)
                elif char == '-':
                    stack.append(num1 - num2)
                elif char == '*':
                    stack.append(num1 * num2)
                elif char == '/':
                    #stack.append(num1 // num2 if num1 * num2 > 0 else -(abs(num1) // abs(num2)))
                    stack.append(int(num1 / num2))
        return stack[-1] if stack else 0
