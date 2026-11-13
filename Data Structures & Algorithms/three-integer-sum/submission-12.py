class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        i = 0
        while i < len(nums):
            right = len(nums) - 1
            left = i + 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif temp > 0:
                    while right - 1 >= 0 and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                else:
                    while nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
            
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        
        return res
