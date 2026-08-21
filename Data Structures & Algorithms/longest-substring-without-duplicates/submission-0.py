class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = {}
        left = 0
        count = 0

        for right in range(len(s)):
            if s[right] in store:
                left = max(store[s[right]] + 1, left)
            store[s[right]] = right
            count = max(count, right - left + 1)
        return count
       

        