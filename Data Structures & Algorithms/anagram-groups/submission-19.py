from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def count(s): 
            counts = [0] * 26
            for c in s:
                counts[ord(c)- ord("a")] += 1
            return tuple(counts)
        hashmap = defaultdict(list)
        for s in strs: 
            hashmap[count(s)].append(s)
        
        return (list(hashmap.values()))