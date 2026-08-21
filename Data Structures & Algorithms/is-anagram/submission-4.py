class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_letters = collections.Counter(s)

        t_letters = collections.Counter(t)

        return s_letters == t_letters


        
        