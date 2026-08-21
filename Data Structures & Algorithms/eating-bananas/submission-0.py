class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        res = right

        while left <= right:
            middle = (left + right) // 2
            time = 0

            for pile in piles:
                time += math.ceil(float(pile) / middle)
                
            if time <= h:
                res = middle
                right = middle - 1
            else:
                left = middle + 1
        return res
            




        