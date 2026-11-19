class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = defaultdict(int)

        res = 0

        for i in range(len(s)):
            freq[s[i]] += 1
            while left < len(s) and i - left + 1 - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
            res = max(res, i - left + 1)
        
        return res