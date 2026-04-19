class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == "": 
            return 0
        elif len(set(s)) == len(s):
            return len(s)
        
        output = 1
        stack = ""

        l, r = 0, 1

        while r < len(s):
            sub = s[l:r]
            curr = s[r]
            if curr in sub:
                output = max(output, len(sub))
                sub = ""
                l += 1
                r = l+1
            else: 
                r = r + 1
                sub = sub + curr
        
        if sub != "" and len(set(sub)) == len(sub):
            return max(output, len(sub))
            
            
        return (output)
            



            