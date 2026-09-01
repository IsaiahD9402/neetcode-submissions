class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_letters = collections.Counter(s)

        t_letters = collections.Counter(t)

        print(s_letters)
        print(t_letters)

        return s_letters == t_letters


        
        