class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0

        seen = {}
        ans = 0

        for r in range(len(s)):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            seen[s[r]] = r
            ans = max(ans, r - l + 1)
        return ans

