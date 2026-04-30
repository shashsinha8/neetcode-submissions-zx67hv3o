class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = {}
        freq = [[] for _ in range(len(nums) + 1)]

        # for i, n in enumerate(nums):
        #     mp[n] = mp.get(n, 0) + 1
        for num in nums:
            mp[num] = 1 + mp.get(num, 0)
        
        for key, v in mp.items():
            freq[v].append(key)
        
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans

        # temp = sorted(mp, key=lambda x: mp[x], reverse=True)
    
        