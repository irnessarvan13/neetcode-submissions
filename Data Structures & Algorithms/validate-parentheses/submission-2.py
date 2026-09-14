class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", 
                        "]" : "[", 
                        "}" : "{" }

        for c in s: #Loop through each charachter
            if c in closeToOpen:    #checking to see if c is a key in closeToOpen!!!
                if stack and stack[-1] == closeToOpen[c]: #First check if stack is not empty and then make sure the value at the top of the stack is the matching opening parantheses
                    stack.pop()
                else: #If they dont match each other or the stack is empty return false
                    return False
            else:     #IF this is a opening parantheses we are going to add it to the stack. Meaning it is NOT a key, it is a value
                stack.append(c)

        return True if not stack else False  #If not stack means return true if stack is empty otherwise return false

        