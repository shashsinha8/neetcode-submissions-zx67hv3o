class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_map = {}

        for i in range(len(nums)):
            count_map[nums[i]] = count_map.get(nums[i], 0) + 1
        
        freq_map = [[] for _ in range(len(nums)+1)]

        for number, v in count_map.items():
            freq_map[v].append(number)
        

        ans = []
        for i in range(len(freq_map)-1, -1, -1):
            for j in range(len(freq_map[i]) -1, -1, -1):
                if len(ans) == k:
                    break
                else:
                    ans.append(freq_map[i][j])
        return ans