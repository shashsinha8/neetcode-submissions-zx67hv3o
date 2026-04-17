class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # clean = [c.lower() for c in s if c.isalnum()]
        # print(clean)

        # return clean == clean[::-1]

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True