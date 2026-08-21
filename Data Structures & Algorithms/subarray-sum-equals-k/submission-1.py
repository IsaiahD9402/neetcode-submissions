class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = { 0 : 1}

        for n in nums:
            curSum += n
            res += prefixSums.get(curSum - k, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        
        return res