class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]
        # prefix > [1, 2, 8, 48]
        # suffix > [48, 48, 24, 6]
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        res = [1] * len(nums)    

        # prefix
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i] * prefix[i - 1]

        # suffix
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffix[i] = nums[i]
            else:
                suffix[i] = nums[i] * suffix[i + 1]

        for i in range(len(res)):
            if i == 0:
                res[i] = suffix[i + 1]
            elif i == len(res) - 1:
                res[i] = prefix[i - 1]
            else:
                res[i] = prefix[i - 1] * suffix[i + 1]

        return res
