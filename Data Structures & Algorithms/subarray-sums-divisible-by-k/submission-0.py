class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        res = 0
        runningSum = 0

        for i in nums:
            runningSum += i

            res += prefix[runningSum % k]

            prefix[runningSum % k] += 1
        
        return res