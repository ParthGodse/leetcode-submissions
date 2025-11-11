class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        prev_low = prices[0]
        count  = 0

        for i in range(1, n - 1):
            # valley
            if prices[i] <= prices[i - 1] and prices[i] <= prices[i + 1]:
                prev_low = prices[i]

            # peak
            elif prices[i] > prices[i - 1] and prices[i] >= prices[i + 1]:
                count += (prices[i] - prev_low)

        # handle boundary peak at end
        if prices[-1] > prices[-2]:
            count += (prices[-1] - prev_low)

        return count