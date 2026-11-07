class Node:

    def __init__(self, key: int, value: int):
        self.key, self.val = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove a node from doubly linked list
    def remove(self, key: int):
        prev, nxt = self.cache[key].prev, self.cache[key].next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.next, node.prev = nxt, prev
        prev.next = nxt.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # remove
        self.remove(key)

        # insert back into cache
        self.insert(self.cache[key])

        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])

        lru = self.left.next

        if len(self.cache) > self.cap:
            self.remove(lru.key)
            del(self.cache[lru.key])
