class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = max(prices[right] - prices[left], profit)

            right += 1
        
        if profit < 0:
            return 0
        
        return profit


        