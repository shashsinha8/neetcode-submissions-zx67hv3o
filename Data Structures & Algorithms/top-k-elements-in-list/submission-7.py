from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_hash = {}
        for i, n in enumerate(nums):
            count_hash[n] = count_hash.get(n, 0) + 1

        print(count_hash)

        sorted_items = sorted(count_hash.items(), key=lambda item: item[1], reverse=True)

        answer = []
        print(sorted_items)

        for key, v in sorted_items: 
            if len(answer) == k:
                return answer
            answer.append(key)
        
        return answer


