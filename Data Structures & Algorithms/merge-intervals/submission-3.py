class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # prev = 0
        # for array in intervals: 
            
        #     if prev 
        if not intervals: 
            return

        intervals = sorted(intervals, key=lambda x: x[0])
        # print(intervals)
        ans = []
        prev = intervals[0]
        for array in intervals: 
            if array[0] <= prev[1]:
                prev[1] = max(prev[1],array[1])
            else: 
                ans.append(prev)
                prev = array
        ans.append(prev)
        return (ans)
