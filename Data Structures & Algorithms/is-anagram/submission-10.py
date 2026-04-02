class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # If the length is not the same return False
        if len(s) != len(t):
            return False
        
        # Create count maps for each string
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        return countS == countT














        # if len(s) != len(t):
        #     return False
        
        # countS, countT = {}, {}

        # for i in range(len(s)):
            
        #     # if s[i] in countS:
        #     #     countS[s[i]] +=1
        #     # else:
        #     #     countS[s[i]] = 1
        #     # countS[s[i]]
            
        #     # if t[i] in countT:
        #     #     countT[t[i]] +=1
        #     # else:
        #     #     countT[t[i]] = 1

        #     countS[s[i]] = countS.get(s[i], 0) + 1
        #     countT[t[i]] = countT.get(t[i], 0) + 1

        # return countS == countT
        # '''
        # s = {
        #     r = 2
        #     a = 2
        #     c = 2
        #     e = 1
        # }

        # t = {
        #     r = 2
        #     a = 2
        #     c = 2
        #     e = 1
        # }
        # '''
        
        
        # # return sorted(s) == sorted(t)
        

        # # print(s[::-1])