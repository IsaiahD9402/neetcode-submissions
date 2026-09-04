class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for ch in string:
                count[ord(ch) - ord('a')] += 1
            
            groups[tuple(count)].append(string)

        #print(groups)

        print(ord('a'))

        return list(groups.values())