class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for n in nums: 
            counts[n] = counts.get(n, 0) + 1
        
        # print(counts)
        freq = [[] for i in range(len(nums)+1)]

        for n, v in counts.items():
            freq[v].append(n)
        
        print(freq)
        ans = []
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                if len(ans) == k:
                    return ans
                else: 
                    ans.append(n)
        
        return (ans)
