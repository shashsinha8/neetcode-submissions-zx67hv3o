class Solution:
    def maxArea(self, heights: List[int]) -> int:

        
        l, r = 0, len(heights) - 1
        ans = 0

        while l < r: 
            volume = min(heights[l], heights[r]) * (r-l)
            ans = max(ans, volume)
            print(f"Volume = {volume}, l = {heights[l]}, r = {heights[r]}")

            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else: 
                l += 1
                r -= 1
        
        return (ans)
            