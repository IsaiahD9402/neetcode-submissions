class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        total = len(countT)
        res, length = [-1, -1], float("infinity")
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                total -= 1
            
            while total == 0:
                if (right - left + 1) < length:
                    res = [left, right]
                    length = right - left + 1
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    total += 1
                left += 1
        left, right = res
        return s[left:right+1] if length != float("infinity") else ""


