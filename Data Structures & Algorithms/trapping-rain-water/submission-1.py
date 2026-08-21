class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left = 0
        right = len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]
        res = 0

        while left < right:
            if maxLeft <= maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                res += maxLeft - height[left]
            if maxRight < maxLeft:
                right -= 1
                maxRight = max(maxRight, height[right])
                res += maxRight - height[right]
            
        return res





        