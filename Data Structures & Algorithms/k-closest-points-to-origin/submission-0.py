
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []

        for x, y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)

        for _ in range(k):
            coord = heapq.heappop(minHeap)
            res.append(coord[1:3])

        return res