class Solution:
    def isValid(self, s: str) -> bool:
        self.stack = []

        for charachter in s:
            if charachter in "({[":
                self.stack.append(charachter)
            elif charachter in ")}]":
                if not self.stack:
                    return False
    
                top = self.stack.pop()

                if top == '(' and charachter == ')':
                    print(top, charachter)
                elif top == '{' and charachter == '}':
                    print(top, charachter)
                elif top == '[' and charachter == ']':
                    print(top, charachter)
                else:
                    return False
        if len(self.stack) == 0:
            return True
        else:
            return False

        