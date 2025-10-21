class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()  # key -> node
        
        # Dummy head and tail to avoid empty states
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        pass
        
    def _add_to_front(self, node: Node) -> None:
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


# Demo
if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))       
    cache.put(3, 3)           
    print(cache.get(2))       
    cache.put(4, 4)           
    print(cache.get(1))       
    print(cache.get(3))       
    print(cache.get(4))       
