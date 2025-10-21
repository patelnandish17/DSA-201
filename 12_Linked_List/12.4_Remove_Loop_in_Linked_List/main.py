

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeLoop(self, head: ListNode) -> None:
        pass

    def printList(self, head: ListNode) -> None:
        pass

# Demo
if __name__ == "__main__":
    # Direct simple node creation and linking
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = head.next  # create loop

    sol = Solution()
    sol.removeLoop(head)
    sol.printList(head)
