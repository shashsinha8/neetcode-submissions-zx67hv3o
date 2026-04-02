from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        answer = defaultdict(int)
        for n in nums: 
            answer[n] += 1
        
        # pair_tuple = [(key, answer[key]) for key in answer.keys()]
        # print(pair_tuple)

        # sorted_tups = sorted(pair_tuple, key = lambda x: -x[1])
        # print(sorted_tups)
        
        # final = []

        # for i in range(k): 
        #     final.append(sorted_tups[i][0])

        # final = [e[0] for e in sorted_tups[:k]]
        
        # return final
        # chatgpt answer

        
        print(answer.items())
        
        final = sorted(answer.items(), key=lambda x: x[1], reverse=True)

        return [num for num,freq in final[:k]]
            

        # return [num for num, freq in sorted_items[:k]]
