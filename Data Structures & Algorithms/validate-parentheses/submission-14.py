class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stack = []

        for c in s: 
            if c in mp:
                if not stack or stack[-1] != mp[c]:
                    return False
                stack.pop()
            else: 
                stack.append(c)
        
        if not stack:
            return True
        else: 
            return False
