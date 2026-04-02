class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strdict = {}
        for s in strs: 
            key = tuple(sorted(s))

            strdict[key] = strdict.get(key,[])
            strdict[key].append(s)

        return strdict.values()