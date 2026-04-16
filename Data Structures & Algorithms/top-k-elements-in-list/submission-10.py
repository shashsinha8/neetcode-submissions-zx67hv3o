class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_map = {}

        for n in nums: 
            count_map[n] = count_map.get(n, 0) + 1

        sorted_count_map = sorted(count_map, key=lambda x: count_map[x], reverse=True)
        return (sorted_count_map[:k])
