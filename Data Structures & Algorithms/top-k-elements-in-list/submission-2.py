import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # count = {}
        # for n in nums: 
        #     count[n] = count.get(n,0) + 1

        # heap = [(-freq,num) for num,freq in count.items()]
        # # heap = []
        # # for num, freq in count.items(): 
        # #     heap.append((-freq,num))

        # heapq.heapify(heap)


        # result = []
        # for _ in range(k):
        #     result.append(heapq.heappop(heap)[1])

        # return result
        

        #method 2 buckets

        count = {}
        for n in nums: 
            count[n] = count.get(n, 0) + 1

        freq = [[] for i in range(len(nums)+ 1)]
        
        for n, c in count.items():
            freq[c].append(n)
        
        result = []
        for i in range(len(freq) - 1, 0 , -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k: 
                    return result






