"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}
        q = collections.deque()
        q.append(node)

        while q and node:
            tempNode = q.popleft()

            if tempNode not in clones:
                copy = Node(tempNode.val)
                clones[tempNode] = copy
            else:
                copy = clones[tempNode]
            
            for n in tempNode.neighbors:
                if n not in clones:
                    nCopy = Node(n.val)
                    copy.neighbors.append(nCopy)
                    clones[n] = nCopy
                    q.append(n)
                else:
                    copy.neighbors.append(clones[n])
            

        return clones[node] if clones else None
