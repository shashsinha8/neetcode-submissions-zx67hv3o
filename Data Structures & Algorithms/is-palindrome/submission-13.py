class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # clean = [c.lower() for c in s if c.isalnum()]
        # print(clean)

        # return clean == clean[::-1]

        l, r = 0, len(s) - 1
        s = s.lower()
        while l < r:
            
            while s[l] == " " or not s[l].isalnum() and l < r:
                l += 1
            while s[r] == " " or not s[r].isalnum() and r > l:
                r -= 1
            if l >= r:
                break
            if s[l] != s[r]:
                return False
            else: 
                l+=1
                r-=1
        return True               
# s="no lemon, no melon"
# l, r = 8, 9
# ,  