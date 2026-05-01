class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nset = set(nums)
        answer = 0

        for n in nset: 
            
            if n-1 in nset: 
                continue
            
            counter = 0
            local = n
            while local in nset:
                counter += 1
                local += 1
                print(f"local = {local}")
            answer = max(answer, counter)
        
        return (answer)

