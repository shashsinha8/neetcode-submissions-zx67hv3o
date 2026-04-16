class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        count_map = defaultdict(list)


        for s in strs: 
            count_map[tuple(sorted(s))].append(s)
        
        # print(count_map.items()) 
        answer = []
        for k in count_map:
            answer.append(count_map[k])

        return answer
