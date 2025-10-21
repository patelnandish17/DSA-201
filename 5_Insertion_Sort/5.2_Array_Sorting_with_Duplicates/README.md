# Array Sorting with Duplicates
**Topic:** Insertion Sort

**Type:** Home Challenge

Problem :

 Sort Array By Parity Given an array of integers nums, sort the array using insertion sort such that all even numbers come before all odd numbers. 

Numbers with the same parity can appear in any order (relative order doesn’t matter). 

Use insertion sort to maintain stability, inserting each element into the correct parity group by shifting others right. This problem mimics sorting by a custom key (parity), similar to ordering records by category in a PostgreSQL-backed microservice. It introduces handling duplicates and custom comparison logic. Constraints: 

1 ≤ nums.length ≤ 5 × 10^4 

0 ≤ nums[i] ≤ 10^9 Example: 

Input: nums = [3,1,2,4] 

Output: [2,4,3,1] (or any order where evens [2,4] precede odds [3,1]) Why It Fits: Requires adapting insertion sort to a binary condition (even/odd), reinforcing key-based sorting while keeping array operations simple. 

 

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
