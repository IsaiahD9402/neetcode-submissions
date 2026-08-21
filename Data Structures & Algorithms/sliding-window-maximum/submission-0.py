class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        largest = 0
        res = []
        num = []
        left = 0

        # So start at 0, 0. Go until 3, then move both

        for right in range(len(nums)):
            num.append(nums[right])
            if right - left + 1 == k:
                res.append(max(num))
                num.pop(0)
                left += 1
        return res

        