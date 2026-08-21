class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        res = []

        while right > left: 
            print(1)

            if numbers[right] + numbers[left] == target:
                res.append(left+1)
                res.append(right+1)
                return res

            while numbers[right] + numbers[left] > target:
                right -= 1
            while numbers[right] + numbers[left] < target:
                left += 1
        