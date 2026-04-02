class Solution:
    def isAlphaNumStrip(self, s: str):
        newstr = ''
        for c in s:
            if 'A'<= c <='Z':
                c = chr(ord(c) + 32)
            if c.isalnum() and c != ' ':
                newstr += c
        return newstr

    def isPalindrome(self, s: str) -> bool:
        
        newstr = self.isAlphaNumStrip(s)
        print(newstr)
        return newstr == newstr[::-1]