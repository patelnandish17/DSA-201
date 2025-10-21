# Remove Nth Node from End of List
# Topic: Linked List
# Type: Home Challenge
from typing import Optional

class ListNode: 
    def __init__(self, val=0, next=None): 
        self.val = val 
        self.next = next 
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Implement two-pointer removal technique
        # Hint: Use dummy node to handle edge case of removing head
        pass

# Demo
if __name__ == "__main__":
    sol = Solution()
    # Example: create linked list and test removeNthFromEnd
