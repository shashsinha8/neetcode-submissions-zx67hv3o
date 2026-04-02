class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mappings = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        '''
        "([{}])"
        "[(])"
        "()[]{}"
        ""
        "("
        ")"


        stack =
        c = )


        '''
 

        for c in s: 
            if c in mappings:
                if not stack:
                    return False 
                if stack[-1] != mappings[c]:
                    return False
                else: 
                    stack.pop()
            else:
                stack.append(c)
         
        if not stack:
            return True
        else: 
            return False