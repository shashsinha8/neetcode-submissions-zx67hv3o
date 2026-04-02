class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit, l = 0, 0
        for r in range(len(prices)):
            tempProfit = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
            if profit < tempProfit:
                profit = tempProfit
                print(profit)
        return profit
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # profit, l = 0, 0
        # r = 1
        # for r in range(len(prices)): 
        #     currentPrice = prices[r] - prices[l]
        #     if prices[r] < prices[l]:
        #         l = r
            
        #     if profit < currentPrice:
        #         profit = prices[r] - prices[l]
        #         print(profit)
            
        # return profit

