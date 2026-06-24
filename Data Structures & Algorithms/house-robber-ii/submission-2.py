class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = 0
        memo = {}
        def dfs(i,flag):
            last = (len(nums) - 1) if flag else (len(nums)-2)

            if i > last:
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = max(dfs(i+1, flag), nums[i] + dfs(i+2, flag))
            return memo[i]
        if len(nums) == 1:
            return nums[0]
            
        val1 = dfs(0, False)
        memo = {}
        val2 = dfs(1, True)
        return max(val1, val2)