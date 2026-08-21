# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortHelper(pairs, 0, len(pairs) - 1)
    def quickSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        if s >= e:
            return pairs
        
        pivot = e
        insert_ptr = s

        for i in range(s, e):
            if pairs[i].key < pairs[pivot].key:
                tmp = pairs[i]
                pairs[i] = pairs[insert_ptr]
                pairs[insert_ptr] = tmp
                insert_ptr += 1
        
        pairs[insert_ptr], pairs[pivot] = pairs[pivot], pairs[insert_ptr]

        self.quickSortHelper(pairs, s, insert_ptr - 1)
        self.quickSortHelper(pairs, insert_ptr + 1, e)

        return pairs