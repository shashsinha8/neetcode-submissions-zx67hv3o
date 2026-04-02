class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # listoflist = []
        
        # for i in range(len(strs)):
        #     strlist = []
        #     strlist.append(strs[i])
        #     for j in range(lens(strs)):
        #         if sorted(strs[i])

        ans = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()