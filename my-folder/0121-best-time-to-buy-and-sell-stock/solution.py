class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxprofit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         if profit > maxprofit:
        #             maxprofit = profit
        # return maxprofit  
        maxprofit = 0
        minprice = float('inf')
        for price in prices:
            if price<minprice:
                minprice = price
            curr_profit = price - minprice
            if curr_profit > maxprofit:
                maxprofit = curr_profit
        return maxprofit
