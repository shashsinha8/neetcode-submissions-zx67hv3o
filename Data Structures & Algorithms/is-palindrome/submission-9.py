class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean = [c.lower() for c in s if c.isalnum()]
        print(clean)

        return clean == clean[::-1]