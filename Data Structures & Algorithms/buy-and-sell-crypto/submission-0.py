class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        for i in prices:
            if i < lowest:
                lowest = i
            if profit < i - lowest:
                profit = i - lowest
        return profit