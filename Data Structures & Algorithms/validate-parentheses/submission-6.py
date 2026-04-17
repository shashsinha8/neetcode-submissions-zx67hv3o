class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closed = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        '''
        stack =
        [
        
        '''
        for c in s: 
            if c in closed:
                if not stack: 
                    return False
                if stack[-1] == closed[c]:
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(c)
        if len(stack) != 0: 
            return False
        else: 
            return True