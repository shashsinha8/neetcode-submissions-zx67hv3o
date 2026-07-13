class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        l = 0
        maxp = 0
        for r in range(len(prices)):
            p = prices[r] - prices[l]
            maxp= max(maxp, p)
            if prices[r] < prices[l]: 
                l = r
        
        return (maxp)
            