class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.tail.prev = self.head
        self.head.next = self.tail
        self.keys = {}
        

    def get(self, key: int) -> int:
        if key in self.keys:
            node = self.keys[key]
            self.touchNode(key, node.val)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.touchNode(key, value)
        else:
            node = Node(key, value)
            if len(self.keys) == self.capacity:
                remove = self.tail.prev
                self.tail.prev = remove.prev
                self.tail.prev.next = self.tail
                del self.keys[remove.key]
            
            if self.tail.prev == self.head:
                self.tail.prev = node
                node.next = self.tail
            else:
                self.head.next.prev = node
                node.next = self.head.next
            self.head.next = node
            node.prev = self.head
                
            self.keys[key] = node
            
            
    def touchNode(self, key, value):
        node = self.keys[key]
        node.val = value
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        

class Node:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
