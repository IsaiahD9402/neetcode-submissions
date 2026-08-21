class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # how my thought process works,
        # create two hash maps, key: char, val: apperances
        # then check the two hash maps against each other


        map1 = dict()
        map2 = dict()


        for i in s:
            map1[i] = map1.get(i, 0) + 1

        for i in t:
            map2[i] = map2.get(i, 0) + 1

        return map1 == map2 
        