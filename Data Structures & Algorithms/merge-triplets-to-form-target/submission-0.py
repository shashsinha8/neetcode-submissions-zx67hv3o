class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        if len(triplets) == 1: 
            return triplets[0] == target


        ans = [0,0,0]
        for i in range(len(triplets)):
            if (triplets[i][0] <= target[0] and
                triplets[i][1] <= target[1] and
                triplets[i][2] <= target[2]):
                ans = [max(triplets[i][0], ans[0]), max(triplets[i][1], ans[1]), max(triplets[i][2], ans[2])]
        
        return ans == target

            