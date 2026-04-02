from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # strs_hash = {[] for n in len(strs)}
        strs_hash  = defaultdict(list)


        for s in strs: 
            sort_s = tuple(sorted(s))
            strs_hash[sort_s].append(s)
            
        # print(strs_hash.values())
        answer = [[] for _ in range(len(strs_hash))]
        

        for i, k in enumerate(strs_hash): 
            answer[i] = strs_hash[k]

        return answer

