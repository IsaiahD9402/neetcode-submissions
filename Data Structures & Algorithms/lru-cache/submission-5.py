class Node:
    def __init__(self, key: int, val: int):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key, value)
            self.cache[key] = node
        else:
            node = self.cache[key]
            node.val = value
            self.remove(node)
        self.insert(node)

        while self.cap < len(self.cache):
            node = self.left.next
            self.remove(node)
            del self.cache[node.key]

    def insert(self, node: Node):
        self.right.prev.next, node.prev = node, self.right.prev
        self.right.prev, node.next = node, self.right

    def remove(self, node: Node):
        node.prev.next, node.next.prev = node.next, node.prev
