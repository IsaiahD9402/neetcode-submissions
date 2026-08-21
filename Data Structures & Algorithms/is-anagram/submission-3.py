class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_letters = collections.Counter(s)

        t_letters = collections.Counter(t)

        result = False

        for letter in s_letters:
            if letter in t_letters and s_letters[letter] == t_letters[letter]:
                result = True
            else:
                return False

        for letter in t_letters:
            if letter in s_letters and s_letters[letter] == t_letters[letter]:
                result = True
            else:
                return False

        
        return result


        
        