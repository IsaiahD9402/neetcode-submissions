class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = [[] for n in range(len(nums) + 1)]
        res = []
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        for n in count:
            frequency[count[n]].append(n)

        right = len(nums) - 1

        while len(res) < k:
            if frequency[right]:
                for n in frequency[right]:
                    res.append(n)
            right -= 1

        return res