class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Given: 
            string s contating parenthesis = '{','[','('
        Task: 
            check if string has valid parenthesis with proper
            opening and closign of each

            Validity rules: 
                - every open bracket is closed by the same type of close bracket.
                - Open brackets are closed in the correct order.
                - Every close bracket has a corresponding open bracket of the same type.
        '''

        stack = []  # Stack to keep track of opening brackets
        mapping = {')': '(', '}': '{', ']': '['}  # Mapping of closing to opening brackets
        
        for char in s:
            if char in mapping:  # If it's a closing bracket
                # Pop from the stack if not empty, 
                # otherwise use a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches 
                # the expected opening bracket
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were properly matched
        return not stack
            