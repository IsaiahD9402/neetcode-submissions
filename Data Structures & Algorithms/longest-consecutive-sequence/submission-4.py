class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # [2,20,4,10,3,4,5]
        # res = 4 [2, 3, 4, 5]

        seen = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in seen:
                seq = 1
                count = n
                while count + 1 in seen:
                    seq += 1
                    count += 1
                res = max(seq, res)

        return res