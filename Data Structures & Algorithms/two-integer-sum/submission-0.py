class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNums = {}
        res = []
        for i, j in enumerate(nums):
            if target - j in hashNums:
                res = [hashNums[target - j], i]
            hashNums[j] = i
        return res 
            
