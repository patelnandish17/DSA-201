import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        # Define less than for ListNode to be used in heapq
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        pass

# Demo (simple example)
if __name__ == "__main__":
    # Construct linked lists: [1->4->5], [1->3->4], [2->6]
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    
    sol = Solution()
    merged = sol.mergeKLists([l1, l2, l3])
    
    # Print merged list
    curr = merged
    while curr:
        print(curr.val, end=" -> " if curr.next else "")
        curr = curr.next
