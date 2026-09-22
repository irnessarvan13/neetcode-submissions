class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            if val == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif val == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif val == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif val == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))  # truncate toward zero
            else:
                stack.append(int(val))
    
        return stack[0]

        