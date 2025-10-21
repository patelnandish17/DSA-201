# Remove Nth Node from End of List
**Topic:** Linked List

**Type:** Home Challenge

Problem :

 Given the head of a linked list, remove the nth node from the end of the list and return its head. This problem tests mastery of the fast-slow pointer technique and edge case handling (e.g., removing head). The optimal solution should traverse the list only once using a two-pointer approach with n-node gap between pointers. 

Example: 

 Input: head = [1, 2, 3, 4, 5], n = 2 

 Output: [1, 2, 3, 5] 

 Explanation: The 2nd node from the end is 4. After removing it, the list becomes [1, 2, 3, 5]. 

Input: head = [1], n = 1 

 Output: [] 

 Explanation: Removing the only node results in an empty list. 

Input: head = [1, 2], n = 2 

 Output: [2] 

 Explanation: The 2nd node from the end is 1 (the head). After removal, only node 2 remains. 

 

Input: head = [1, 2, 3], n = 1 

 Output: [1, 2] 

 Explanation: The 1st node from the end is 3 (the tail). After removing it, the list is [1, 2]. 

Input: head = [10, 20, 30, 40], n = 4 

 Output: [20, 30, 40] 

 Explanation: The 4th node from the end is 10 (the head). After removal, the list starts at 20. 

Input: head = [5, 5, 5, 5, 5], n = 3 

 Output: [5, 5, 5, 5] 

 Explanation: The 3rd node from the end is removed. Even with duplicates, position-based removal works correctly. 

Input: head = [100, 200, 300], n = 1 

 Output: [100, 200] 

 Explanation: The last node (300) is removed, leaving [100, 200]. 

Constraints: 

1 ≤ length of list ≤ 10^4 

1 ≤ n ≤ length of list 

Node values are integers 

Aim for single-pass solution 

### Approach
Describe your approach here...

### Pseudocode
```
Write your pseudocode here...
```

### Time Complexity
- 

### Space Complexity
- 
