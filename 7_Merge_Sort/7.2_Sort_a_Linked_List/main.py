# Sort a Linked List
# Topic: Merge Sort
# Type: Home Challenge

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass
# Demo
if __name__ == '__main__':
    # Helper function to convert list to linked list
    def list_to_linked(lst):
        dummy = ListNode(0)
        cur = dummy
        for val in lst:
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next
    
    # Helper function to convert linked list to list
    def linked_to_list(head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res
    
    sol = Solution()
    head = list_to_linked([4,2,1,3])
    sorted_head = sol.sortList(head)
    print(linked_to_list(sorted_head))  
