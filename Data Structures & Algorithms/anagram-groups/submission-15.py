from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)

        for s in strs: 
            hashmap[self.counter(s)].append(s)

        ans = [v for k, v in hashmap.items()]

        return ans
    
    def counter(self, s): 
        ans = [0] * 26

        for c in s: 
            ans[ord(c) - ord("a")] += 1
            
        return tuple(ans)