class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        count = defaultdict(list)

        for s in strs:
            c = tuple(sorted(s))
            count[c].append(s)
        
        for val in count.values():
            res.append(val)

        return res
