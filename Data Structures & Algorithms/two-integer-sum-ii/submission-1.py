class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # hashmap = {}

        # for i in range(len(numbers)): 
        #     diff = target - numbers[i]
        #     if diff in hashmap:
        #         return [hashmap[diff]+1, i+1]
        #     # hashmap.get(numbers[i])
        #     hashmap[numbers[i]] = i

        l = 0
        r = len(numbers) - 1

        while numbers[l] + numbers[r] != target:

            summ = numbers[l] + numbers[r]
            if summ > target: 
                r -= 1
            else: 
                l += 1
        
        return [l+1, r+1]
