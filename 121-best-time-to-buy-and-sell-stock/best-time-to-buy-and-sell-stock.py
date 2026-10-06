class Solution(object):
    def maxProfit(self, prices):
        min_prices=prices[0]
        profit=0
        for i in range(1,len(prices)):
            curr_prices=prices[i]-min_prices
            if curr_prices>profit:
                profit=curr_prices
            min_prices=min(min_prices,prices[i])    
        return profit    
                 