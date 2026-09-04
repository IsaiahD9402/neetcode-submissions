class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for string in strs:
            groups["".join(sorted(string))].append(string)

        #print(groups)

        return list(groups.values())