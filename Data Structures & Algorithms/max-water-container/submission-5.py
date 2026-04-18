class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        [1,7,2,5,4,7,3,6]
        l = 0 
        r = len(height) - 1
        length = r - l

        Area = smaller height * length
        '''

        l = 0 
        r = len(heights) - 1
        
        answer = 0

        while l < r:
            
            length = r - l
            smaller = min(heights[l], heights[r])
            area = smaller * length
            answer = max(answer, area)
            if heights[l] == smaller: 
                l += 1
            else: 
                r -= 1
    
        return answer
