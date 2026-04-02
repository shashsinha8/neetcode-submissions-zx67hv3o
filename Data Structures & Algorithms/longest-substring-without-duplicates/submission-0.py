class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        ans = 0
        
        for i, c in enumerate(s): 
            j = i
            substring = ''
            while j < len(s) and s[j] not in substring: 

                substring += s[j]
                j += 1
                # print(f"i = {i} | substr = {substring}")
            # print(f"i = {i} | substr = {substring}")
            if ans < len(substring): ans = len(substring)
        
        return ans
        
