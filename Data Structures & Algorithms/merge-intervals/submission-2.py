class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for n in range(1, len(intervals)):
            if intervals[n][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[n][1])
            else:
                res.append(intervals[n])
            

        return res