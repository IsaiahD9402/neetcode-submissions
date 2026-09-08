class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i, n in enumerate(nums):
            prefix[i] = 1 * n if i < 1 else 1 * n * (prefix[i - 1]) 
        
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = 1 * nums[i] if i == len(nums) - 1 else nums[i] * suffix[i + 1]

        res = [1] * len(nums)

        for i in range(len(res)):
            if i == 0:
                res[i] = suffix[1]
            elif i == len(nums) - 1:
                res[i] = prefix[i - 1]
            else:
                res[i] = prefix[i - 1] * suffix[i + 1]

        #print(prefix)
        #print(suffix)

        return res