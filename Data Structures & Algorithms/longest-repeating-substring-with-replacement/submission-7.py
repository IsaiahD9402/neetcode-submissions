class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)

        res = 0
        left = 0

        for r, c in enumerate(s):
            count[c] += 1
            if (r - left + 1) - max(count.values()) <= k:
                res = max(res, r - left + 1)
            else:
                count[s[left]] -= 1
                left += 1

        return res