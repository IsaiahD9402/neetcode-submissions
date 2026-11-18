# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()

        for i, n in enumerate(lists):
            if n:
                heapq.heappush(heap, (n.val, i, n))
        cur = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

            cur = cur.next

        return dummy.next
