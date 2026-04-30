class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            ans[i] = pre
            pre = pre * nums[i]
            
        print(f"pre = {ans}")
        post = 1
        p = collections.deque()
        for i in range(len(nums)-1, -1, -1):
            p.appendleft(post)
            ans[i] = ans[i] * post
            post = post * nums[i]
        print(f"pos = {[n for n in p]}")
        print(f"ans = {ans}")
        return ans