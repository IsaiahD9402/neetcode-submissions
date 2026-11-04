class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        res = 0
        add = nums.count(k)

        for v in set(nums):
            cur = 0
            if v == k:
                continue
            for n in nums:
                if n == v:
                    cur += 1
                elif n == k:
                    cur -= 1
                
                cur = max(cur, 0)
    
                res = max(res, cur + add)

        
        return res
            