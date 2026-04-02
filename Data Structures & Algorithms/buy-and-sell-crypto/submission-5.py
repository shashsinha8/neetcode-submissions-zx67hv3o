class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        l = 0
        r = 1
        maxp = 0

        '''
        [10,1,5,6,7,1]
        
        l = 0
        r = 1

        l = 10
        r = 1
        
        since r < l: l = r, r = l+1
        
        l = 10
        r = 5

        profit = prices[r] - prices[l]
        check maxprofit: max(maxp, profit)
        '''

        while r < len(prices):            
            if prices[r] < prices[l]: 
                l = r
            
            profit = prices[r] - prices[l]
            maxp = max(maxp, profit)
            r +=1
        
        return maxp



