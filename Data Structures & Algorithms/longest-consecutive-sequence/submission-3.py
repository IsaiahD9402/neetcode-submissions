class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        long = 0

        for num in numSet:
            if (num - 1) not in numSet:
                count = 1
                while (num + count) in numSet:
                    count += 1
                long = max(count, long)
        return long