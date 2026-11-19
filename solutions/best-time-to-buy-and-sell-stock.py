class Solution(object):
    def maxProfit(self, prices):
        maxp = 0
        while(len(prices) > 1):
            m = min(prices)
            id1 = prices.index(m)
            arr = prices[id1:]
            ma  = max(arr)
            if ma - m > maxp:
                maxp = ma-m
            prices = prices[:id1]
        return maxp
        