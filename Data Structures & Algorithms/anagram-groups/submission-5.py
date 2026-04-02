from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)

        for i in range(len(strs)):
            hashmap[tuple(sorted(strs[i]))].append(strs[i])

        return list(hashmap.values())