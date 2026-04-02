class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # stripped = []
        # for c in s: 
        #     if c.isalnum():
        #         stripped.append(c.lower()) # string concatenation BAD
        
        # print(stripped)
        
        # return stripped == stripped[::-1]

        l = 0
        r = len(s) - 1

        while l < r: 
            while l<r and not s[l].isalnum():
                l+=1 
            
            while r>l and not s[r].isalnum():
                r-=1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l+=1
            r-=1
        return True
