class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hash = []

        for i, n in enumerate(nums): 
            if nums[i] in hash: 
                return True
            else: 
                hash.append(n)

        return False
        # print(f"nums: {nums}")
        # print(f"hash: {hash}")