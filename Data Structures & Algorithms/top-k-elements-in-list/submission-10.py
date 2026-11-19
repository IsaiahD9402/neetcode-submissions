class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        freq = collections.Counter(nums)

        for f in freq:
            heapq.heappush(heap, (freq[f], f))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        for i in range(len(heap)):
            frequency, val = heapq.heappop(heap)
            res.append(val)

        return res