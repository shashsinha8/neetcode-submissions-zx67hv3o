class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean = ""
        for c in s.lower():
            if c == " ":
                continue
            elif self.isAlphaNum(c):
                clean += c
        
        return clean == clean[::-1]
        


    def isAlphaNum(self, c):
        if not (
            ord(c) >= ord("a") and ord(c) <= ord("z") or 
            ord(c) >= ord("A") and ord(c) <= ord("Z") or 
            ord(c) >= ord("0") and ord(c) <= ord("9")
        ):
            return False
        return True
