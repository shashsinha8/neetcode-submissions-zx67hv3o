class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = defaultdict(list)

        for s in strs: 
            mp[tuple(sorted(s))].append(s)
        
        return (list(mp.values()))