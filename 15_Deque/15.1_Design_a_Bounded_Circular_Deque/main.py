# Design a Bounded Circular Deque
# Topic: Deque
# Type: In-Session

class MyCircularDeque:
    def __init__(self, k: int):
        pass

    def insertFront(self, value: int) -> bool:
        pass

    def insertLast(self, value: int) -> bool:
        pass

    def deleteFront(self) -> bool:
        pass

    def deleteLast(self) -> bool:
        pass

    def getFront(self) -> int:
        pass

    def getRear(self) -> int:
        pass

    def isEmpty(self) -> bool:
        pass

    def isFull(self) -> bool:
        pass

# Demo
if __name__ == "__main__":
    deque = MyCircularDeque(3)
    print(deque.insertLast(5))   
    print(deque.insertFront(3))  
    print(deque.getRear())      
    print(deque.deleteLast())    
    print(deque.getFront())      
    print(deque.isEmpty())    
