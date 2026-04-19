class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == "": 
            return 0

        output = 1
        sub = set()

        l, r = 0, 1
        sub.add(s[0])

        while r < len(s):
            curr = s[r]
            if curr in sub:
                print(sub)
                sub.remove(s[l])
                l += 1
            else:
                sub.add(curr)
                output = max(output, len(sub))
                r += 1

        return (output)
            



            