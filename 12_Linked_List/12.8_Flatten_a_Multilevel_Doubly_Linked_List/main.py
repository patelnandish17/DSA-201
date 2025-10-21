class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        pass
if __name__ == "__main__":
    # Create list: 1 <-> 2 <-> 3, with 2 having child 4 <-> 5
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    n1.next = n2
    n2.prev = n1
    n2.next = n3
    n3.prev = n2

    n2.child = n4
    n4.next = n5
    n5.prev = n4

    sol = Solution()
    head = sol.flatten(n1)

    # Print flattened list
    curr = head
    while curr:
        print(curr.val, end=" <-> " if curr.next else "\n")
        curr = curr.next
