# Remove Nth Node from End of List (Variant)
# Topic: Linked List
# Type: Home Challenge
from typing import Optional

class ListNode: 
    def __init__(self, val=0, next=None): 
        self.val = val 
        self.next = next 
        
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Implement linked list merge sort
        # Steps: split (find middle), recursive sort, merge
        pass

    def getMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Helper: Find middle node using slow-fast pointer
        pass

    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Helper: Merge two sorted linked lists
        pass

# Demo
if __name__ == "__main__":
    sol = Solution()
    # Example: create linked list and test sortList
