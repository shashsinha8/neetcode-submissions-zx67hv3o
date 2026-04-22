class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        if s == "": 
            return 0
        elif len(s) == 1:
            return 1
            
        # "zxyzxyz"
        # " L R   "
        l = 0
        r = 1
        visited = set()
        visited.add(s[l]) # z,x,y
        maxsub = 0

        while r < len(s):
            if s[r] not in visited: 
                visited.add(s[r])
                r += 1
                maxsub = max(maxsub, len(s[l:r]))
            elif s[r] in visited:
                visited.remove(s[l])
                l += 1
        
        return maxsub
            