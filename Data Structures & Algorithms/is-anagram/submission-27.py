class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # return sorted(s) == sorted(t)
        
        if len(s) != len(t):
            return False


        cts, ctt = {}, {}
        for i in range(len(s)): 
            cts[s[i]] = cts.get(s[i], 0) + 1
            ctt[t[i]] = ctt.get(t[i], 0) + 1
        
        return cts == ctt