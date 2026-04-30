class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:         

        # nums = int array
        # return output 
        # output[i] is the product of all the elements of nums except nums[i]
        
        """
        Input: nums = [1,2,4,6]
        Output: [48,24,12,8]
        input=[1, 2, 4, 6]
        outpu=[48, 24, 12, 8]
        befor=[1, 2, 8, 48]
        after=[48, 48, 24, 6]
        awnse=[]
        """

        before, after= [], [1] * len(nums)

        for i, n in enumerate(nums):
            if not before:
                before.append(1 * nums[i])
            else:
                before.append(before[i - 1] * n)

        for i in range(len(nums) - 1, 0, -1):
            if i == len(nums)-1:
                after[i] = 1 * nums[i]
            else: 
                after[i] = after[i + 1] * nums[i]

        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(after[1])
            elif i == len(nums) -1:
                ans.append(before[len(before)-2])
            else: 
                ans.append(before[i-1]*after[i+1])
        print(f"inp : {nums}")
        print(f"bef : {before}")
        print(f"aft : {after}")
        print(f"ans : {ans}")

        return ans