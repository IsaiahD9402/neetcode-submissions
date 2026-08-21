class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, j in enumerate(nums):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val == 0:
                    if [nums[i], nums[left], nums[right]] not in res:
                        res.append([nums[i], nums[left], nums[right]]) 
                    left += 1
                elif val > 0:
                    right -= 1
                else:
                    left += 1
                    while nums[left] == nums[left - 1]:
                        left += 1
        return res