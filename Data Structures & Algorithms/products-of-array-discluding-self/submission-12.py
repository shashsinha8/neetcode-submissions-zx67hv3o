class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            
        prefix = []
        pre = 1
        for n in nums: 
            prefix.append(pre)
            pre = pre * n
        
        print(prefix)

        postfix = deque()
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix.appendleft(post)
            post = post * nums[i]
        print(postfix)

        for i in range(len(prefix)):
            prefix[i] *= postfix.popleft()

        return prefix
