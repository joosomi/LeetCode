class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        brackets = { ")": "(", "}": "{", "]": "["}
        
        for i in range(len(s)):
            if s[i] in brackets:
                if stack and stack[-1] == brackets[s[i]]:
                    stack.pop() 
                else:
                    return False
            else:
                stack.append(s[i])

        if stack:
            return False
        else:
            return True