class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contains = set()
        res = 0

        left = 0

        for c in range(len(s)):
            while s[c] in contains:
                contains.remove(s[left])
                left += 1
            contains.add(s[c])
            res = max(res, c - left + 1)
            
        return res