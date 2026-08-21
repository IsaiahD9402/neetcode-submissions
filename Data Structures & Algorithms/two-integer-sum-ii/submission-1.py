class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        k = len(numbers) - 1
        res = []
        while not res:
            if numbers[i] + numbers[k] == target:
                res = [i + 1, k + 1]
            elif numbers[i] + numbers[k] > target:
                k -= 1
            else:
                i += 1
        return res