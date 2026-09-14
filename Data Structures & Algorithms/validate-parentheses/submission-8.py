class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", 
                        "]" : "[", 
                        "}" : "{" }

        for char in s:
            if char in closeToOpen:             # it's a closing bracket
                if not stack:
                    return False                # nothing to match with
                if stack[-1] != closeToOpen[char]:  # top of stack doesn't match
                    return False
                stack.pop()                     # it matches, pop it
            else:
                stack.append(char)              # it's an opening bracket, push it

        return len(stack) == 0                  # if stack is empty, all brackets matched

        