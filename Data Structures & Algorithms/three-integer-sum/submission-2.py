class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, j in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val == 0:
                    res.append([nums[i], nums[left], nums[right]]) 

                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and right > left:
                        right -= 1

                elif val > 0:
                    right -= 1
                else:
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res