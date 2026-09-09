class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charMap = defaultdict(int)
        left = 0

        for i, c in enumerate(s):
            charMap[c] += 1
            while i - left - max(charMap.values()) + 1 > k:
                charMap[s[left]] -= 1
                left += 1
            res = max(res, i - left + 1)
            
            
        return res


