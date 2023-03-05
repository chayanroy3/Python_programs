class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price=max(prices)
        overall_profit = 0
        profit=0
        for i in range(0,len(prices)):
            if prices[i] < buy_price:
                buy_price=prices[i]
            profit = prices[i]-buy_price
            if overall_profit < profit:
                overall_profit =profit
        return overall_profit

