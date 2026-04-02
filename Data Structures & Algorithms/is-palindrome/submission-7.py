class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # alphanum = [] 

        # for c in s: 
        #     if c.isalnum():
        #         alphanum.append(c.lower())
        
        # return alphanum == alphanum[::-1]


        '''
        while left < right: 
        Base case 1: while left < right and not s[l].isalnum: left ++
        Base case 2: while right > left and not s[r].isalnum: right --

        check if left lower != right lower: return False


        '''

        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1
            r -=1
        
        return True
                

