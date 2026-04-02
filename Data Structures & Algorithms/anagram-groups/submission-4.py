from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # answer = {}
        # for s in strs:
        #     hashkey = "".join(sorted(s))
        #     answer.setdefault(hashkey, []).append(s)

        # return list(answer.values())
        answer = defaultdict(list)

        for s in strs: 
            hashkey = "".join(sorted(s))
            answer[hashkey].append(s)
        
        return list(answer.values())