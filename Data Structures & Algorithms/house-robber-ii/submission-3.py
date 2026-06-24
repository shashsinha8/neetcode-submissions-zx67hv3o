class Solution:
    def rob(self, nums: List[int]) -> int:

        ans = 0
        memo = {}
        def dfs(i, last):
            if i >= last:
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = max(dfs(i+1, last), nums[i] + dfs(i+2, last))
            return memo[i]
        if len(nums) == 1:
            return nums[0]
            
        val1 = dfs(0, len(nums) - 1)
        memo = {}
        val2 = dfs(1, len(nums))
        return max(val1, val2)