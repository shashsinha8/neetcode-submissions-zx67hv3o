from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def counter(s):
            count = [0] * 26
            for c in s: 
                count[ord(c.lower())-ord("a")] += 1
            return count

        hashmap = defaultdict(list)
        for s in strs:
            hashmap[tuple(counter(s))].append(s)

        
        return list(hashmap.values())