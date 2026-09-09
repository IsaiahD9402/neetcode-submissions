class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        left, right = 0, 1

        while right < len(prices) and left < right:
            res = max(res, prices[right] - prices[left])

            if prices[right] < prices[left]:
                left = right
                right += 1
                continue
            right += 1
            
        
                
        
        return res