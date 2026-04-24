class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        # l = 0
        # visited = set()
        # ans = 0

        # for r in range(len(s)):
        #     while s[r] in visited:
        #         visited.remove(s[l])
        #         l+=1
        #     visited.add(s[r])
        #     ans = max(ans, r - l + 1)

        # return ans     

    
        l = 0
        ans = 0
        seen = {}


        for r in range(len(s)):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            seen[s[r]] = r
            ans = max(ans, r - l + 1)
        return ans


