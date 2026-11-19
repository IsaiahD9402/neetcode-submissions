"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        clones = {node: Node(node.val)}
        q = collections.deque()
        q.append(node)

        while q:
            copy = q.popleft()

            for n in copy.neighbors:
                if n not in clones:
                    q.append(n)
                    clones[n] = Node(n.val)
                clones[copy].neighbors.append(clones[n])
        
        return clones[node]