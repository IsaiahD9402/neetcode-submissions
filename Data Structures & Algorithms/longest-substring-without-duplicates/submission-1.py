class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        left = 0
        count = 0

        for right in range(len(s)):
            while s[right] in store:
                store.remove(s[left])
                left += 1
            store.add(s[right])
            count = max(count, right - left + 1)
        return count
       

        