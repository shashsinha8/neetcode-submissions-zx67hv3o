class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_map = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        
        for n in nums: 
            count_map[n] = 1 + count_map.get(n, 0)
        
        for num, count in count_map.items():
            freq[count].append(num)

        ans = []
        print(f"empty ans length = {len(ans)}")
        for index in range(len(freq) - 1, -1, -1):
            for num in freq[index]:
                if len(ans) == k: 
                    return ans
                ans.append(num)
        return ans