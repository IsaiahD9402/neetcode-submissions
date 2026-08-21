class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a-z case, creating an array of size 26

            for c in s:
                count[ord(c) - ord("a")] += 1 # Here is the index

            result[tuple(count)].append(s) # we need to make it a tuple

        return list(result.values())