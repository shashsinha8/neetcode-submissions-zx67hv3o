import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for n in nums: 
            count[n] = count.get(n,0) + 1

        heap = [(-freq,num) for num,freq in count.items()]
        # heap = []
        # for num, freq in count.items(): 
        #     heap.append((-freq,num))

        heapq.heapify(heap)


        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
        