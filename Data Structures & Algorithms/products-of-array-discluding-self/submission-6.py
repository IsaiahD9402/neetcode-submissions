class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # [1, 2, 3, 4] input
        # [1, 2, 6, 24] prefix
        # [24, 24, 12, 4] suffix
        # [24, 12, 8, 6] result

        # [1, 1, 2, 6] first-pass
        # [24, 12, 8, 6]
        res = []
        count = 1
        for i in nums:
            res.append(count)
            count *= i


        
        count = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] = count * res[i]
            count *= nums[i]

        return res