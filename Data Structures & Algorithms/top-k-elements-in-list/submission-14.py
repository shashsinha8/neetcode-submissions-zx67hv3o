class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = {}

        for i, n in enumerate(nums):
            mp[n] = mp.get(n, 0) + 1

        temp = sorted(mp, key=lambda x: mp[x], reverse=True)
    
        return temp[:k]