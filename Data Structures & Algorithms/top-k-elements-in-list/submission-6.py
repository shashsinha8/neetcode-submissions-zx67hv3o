from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,2,2,3,3,3], k = 2

        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        # print(count)

        freq = [[] for n in range(len(nums)+ 1)]
        for n, c in count.items():
            freq[c].append(n)
        # print(freq)

        result = []

        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
