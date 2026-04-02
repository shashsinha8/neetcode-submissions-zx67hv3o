class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        '''
        Given: 
            prices -> List[int] (stock prices based on i days)
        Goal: 
            return the maximum profit i can get from this array
        prices = [10, 1, 5, 6, 7, 1]
        output = 6 
        '''

        Profit, l = 0, 0

        for r in range(l+1, len(prices)): 

            currentProfit = prices[r] - prices[l]
            
            # check if price[l] < price[r] to update pointers
            if prices[l] > prices[r]:
                l = r

            # check if currentProfit > Profit
            if currentProfit > Profit: 
                Profit = currentProfit
        return Profit
