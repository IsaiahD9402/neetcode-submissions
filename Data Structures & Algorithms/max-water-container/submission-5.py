class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # thinking we use l * height to compute the 
        # total amount of water we can store

        left = 0
        right = len(heights) - 1
        collected = 0
        highest = 0
        length = 0

        while left < right:
            if heights[left] <= heights[right]:
                collected = heights[left] * abs((right - left))
                left += 1
                highest = max(collected, highest)
            
            if heights[left] >= heights[right]:
                collected = heights[right] * abs((left - right))
                right -= 1
                highest = max(collected, highest)
        return highest




        