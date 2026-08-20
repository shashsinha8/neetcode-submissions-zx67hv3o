class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums: 
            count[n] = count.get(n, 0) + 1
        
        # print(count)
        # freq = [[] * len(nums)]
        freq = [[] for _ in range(len(nums)+1)]
        dup = set()
        for n in nums:
            if n not in dup:
                # print(len(freq))
                freq[count[n]].append(n)
            dup.add(n)
        
        # print(freq)
        ans = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                if len(ans) == k: 
                    return ans
                else:
                    ans.append(n)
        return ans
