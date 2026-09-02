class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        
        frequency = [[] for i in range(len(nums) + 1)]

        for val, freq in count.items():
            frequency[freq].append(val)
        
        res = []

        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res