class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = [0] * len(nums)
        res = [0] * len(nums)
        count = 1
        for i in nums:
            count *= i
            prefix.append(count)
        
        count = 1

        for i in range(len(nums) - 1, -1, -1):
            count *= nums[i]
            suffix[i] = count

        for i in range(len(nums)):
            if i == 0:
                res[i] = suffix[i + 1]
            elif i == len(nums) - 1:
                res[i] = prefix[i - 1]
            else:
                res[i] = prefix[i - 1] * suffix[i + 1]
        return res