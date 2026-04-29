from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # def counter(s) -> dict:
        #     mp = {}
        #     for c in s: 
        #         mp[c] = mp.get(c, 0) + 1
        #     return mp

        ans = defaultdict(list)
        for s in strs: 
            ans[tuple(sorted(s))].append(s)
        
        return list(ans.values())