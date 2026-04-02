class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        scount, tcount = {}, {}

        for i in range(len(s)): 
            
            scount[s[i]] = scount.get(s[i], 0) + 1
            tcount[t[i]] = tcount.get(t[i], 0) + 1
        
        return scount == tcount

        








        
        # Basic: 
        # if sorted(s) == sorted(t): 
        #     return True
        # else: 
        #     return False

        # if len(s) != len(t): 
        #     return False

        # smap = {}
        # tmap = {}

        # for i in range(len(s)): 
        #     smap[s[i]] = smap.get(s[i], 0) +1
        #     tmap[t[i]] = tmap.get(t[i], 0) +1
        # if smap == tmap: 
        #     return True
        # return False        
        