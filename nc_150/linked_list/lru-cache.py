class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.m = {}
        self.header = Node(0,0)
        self.trailer = Node(0,0)
        self.header.next = self.trailer
        self.trailer.prev = self.header

    def unlink(self, node:Node): 
        a,b = node.prev, node.next
        a.next = b
        b.prev = a
        node.prev = node.next = None

    def addLast(self, node:Node):
        last_element = self.trailer.prev
        node.prev = last_element
        node.next = self.trailer
        last_element.next = node
        self.trailer.prev = node

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1

        n = self.m[key]
        self.unlink(n)
        self.addLast(n)
        return n.value
        
    def evict_first(self):
        first = self.header.next
        self.unlink(first)
        del self.m[first.key]

    def put(self, key: int, value: int) -> None:
        if key not in self.m and len(self.m) >= self.capacity:
            self.evict_first()

        if key in self.m:
            n = self.m[key]
            n.value = value
            self.unlink(n)
        else:
            n = Node(key, value)
            self.m[key] = n

        self.addLast(n)
