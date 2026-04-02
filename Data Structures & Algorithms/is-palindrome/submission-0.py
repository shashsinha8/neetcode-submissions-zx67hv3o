class Solution:
    def isAlphaNumStrip(self, s: str):
        newstr = ''
        s = s.lower()
        for c in s: 
            if c.isalnum() and c != ' ':
                newstr += c
        return newstr

    def isPalindrome(self, s: str) -> bool:
        
        newstr = self.isAlphaNumStrip(s)
        print(newstr)
        return newstr == newstr[::-1]