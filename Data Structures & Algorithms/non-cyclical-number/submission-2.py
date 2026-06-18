class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        ans = 0
        while(ans not in seen):
            
            seen.add(n)
            ans = 0
            stringnum = str(n)
            for c in stringnum: 
                ans += int(c) ** 2
            
            if ans == 1:
                return True
            else:
                n = ans
        return False