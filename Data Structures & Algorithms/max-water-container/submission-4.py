class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        j = len(heights) - 1
        i = 0
        cur = 0

        while i != j:
            cur = min(heights[i], heights[j]) * (j - i)
            if cur > res:
                res = cur
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        
        return res