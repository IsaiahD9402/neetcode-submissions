class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)]

        hashmap = collections.Counter(nums)

        for c in hashmap:
            count[hashmap[c]].append(c)
        
        res = []

        right = len(nums) - 1

        while len(res) < k:
            if count[right]:
                for n in count[right]:
                    res.append(n)
            right -=1


        return res

  
