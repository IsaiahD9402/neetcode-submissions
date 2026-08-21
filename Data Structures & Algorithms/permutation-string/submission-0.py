class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        chars = [0] * 26
        size = len(s1)

        for c in s1:
            index = ord(c) - ord('a')
            chars[index] += 1
        
        left = 0
        for right in range(len(s2)):
            index = ord(s2[right]) - ord('a')
            chars[index] -= 1

            if right - left + 1 > size:
                index = ord(s2[left]) - ord('a')
                chars[index] += 1
                left += 1
            
            if all(v == 0 for v in chars):
                return True
        
        return False
                

