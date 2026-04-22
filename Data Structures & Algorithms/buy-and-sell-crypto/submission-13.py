class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxp = 0
        l = 0
        r = 1
        if len(prices) == 1:
            return 0

        while r < len(prices):
            p = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
            else:
                maxp = max(p, maxp)
            r += 1
        
        return maxp