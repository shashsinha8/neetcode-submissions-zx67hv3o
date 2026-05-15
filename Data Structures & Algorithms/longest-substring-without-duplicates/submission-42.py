class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        if not s: 
            return 0
        elif len(s) == 1: 
            return 1

        l, r= 0, 0

        char_set = set()
        ans = 0

        while r < len(s):
            
            if s[r] not in char_set:
                char_set.add(s[r])
                r += 1
            elif s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            ans = max(ans, len(char_set))
            
        return ans