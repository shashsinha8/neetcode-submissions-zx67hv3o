class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        count_map = defaultdict(list)
        for s in strs: 
            count_map[self.counter(s)].append(s)
        
        answer = []
        for k in count_map:
            answer.append(count_map[k])

        return answer


    def counter(self, s):
        count =[0]*26
        for c in s:
            count[ord(c) - ord("a")] += 1
        return tuple(count) 
            