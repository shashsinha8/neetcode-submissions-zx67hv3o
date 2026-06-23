class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 1:
            return False        

        stack = []
        
        check = {
            "}":"{",
            "]":"[",
            ")":"(",
        }

        for c in s:
            
            if c not in check: 
                stack.append(c)
            elif c in check:
                if not stack:
                    return False
                elif stack[-1] == check[c]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False

