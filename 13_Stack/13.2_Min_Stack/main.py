# Min Stack
# Topic: Stack
# Type: In-Session

class MinStack:
    def __init__(self):
        # Initialize your stack data structures
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass

# Demo
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  
    minStack.pop()
    print(minStack.top())     
    print(minStack.getMin())  
