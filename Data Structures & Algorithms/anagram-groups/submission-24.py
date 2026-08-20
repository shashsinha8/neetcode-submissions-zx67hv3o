class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def counter(s):
            count = [0] * 26
            for c in s: 
                count[ord(c) - ord("a")] += 1
            return tuple(count)

        mp = defaultdict(list)

        for s in strs: 
            mp[counter(s)].append(s)
        
        return (list(mp.values()))