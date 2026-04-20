class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hash = set()

        for n in nums: 
            if n in hash: 
                return True
            else: 
                hash.add(n)

        return False
        # print(f"nums: {nums}")
        # print(f"hash: {hash}")