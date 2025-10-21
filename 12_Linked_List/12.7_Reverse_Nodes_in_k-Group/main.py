class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pass
    
# Demo
if __name__ == "__main__":
    # List: 1->2->3->4->5, k=2
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
   
    sol = Solution()
    new_head = sol.reverseKGroup(head, 2)
   
    # Print the reversed list in k groups
    curr = new_head
    while curr:
        print(curr.val, end=" -> " if curr.next else "")
        curr = curr.next