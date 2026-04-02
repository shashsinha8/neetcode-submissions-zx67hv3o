class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean = s.replace(' ', '')
        stripped = ''
        for c in s: 
            if c.isalnum():
                stripped += c.lower()
        
        print(stripped)
        
        return stripped == stripped[::-1]
