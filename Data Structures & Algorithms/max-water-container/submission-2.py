class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        k = len(heights) - 1
        i = 0
        val = 0

        while i < k:
            val = min(heights[i], heights[k]) * (k - i)
            res = max(val, res)
            if heights[i] > heights[k]:
                k -= 1
            else:
                i += 1
        
        return res