class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # prefix of modulo of sum
        # [5, 1, 5, 5, 0]

        preDict = defaultdict(int)

        count = 0

        preDict[0] = -1
        for i, n in enumerate(nums):
            count += n
        
            if count % k in preDict and i - preDict[count % k] > 1:
                return True

            if count % k not in preDict:
                preDict[count % k] = i
        
        return False