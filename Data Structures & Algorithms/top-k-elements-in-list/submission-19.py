class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}

        for n in nums: 
            hashmap[n] = hashmap.get(n, 0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        
        for key, v in hashmap.items():
            freq[v].append(key)
        
        
        ans = []
        for i in range(len(freq) - 1, -1, -1): 
            for n in freq[i]:
                print(freq[i])
                print(len(ans), ans)
                ans.append(n) 
                if len(ans) == k:
                    print(f"true: {ans}, {len(ans)} == {k}? ")
                    return ans
        print(ans)