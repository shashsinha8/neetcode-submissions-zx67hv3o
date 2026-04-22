class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxA = 0

        l, r = 0, len(heights) - 1

        while l<r: 
            length = r - l
            height = min(heights[l], heights[r])
            Area = length * height
            maxA = max(maxA, Area)

            if heights[l] < heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1
            else:
                l+=1
                r-=1

        return maxA