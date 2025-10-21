# Array Sorting with Derived Metrics
**Topic:** Insertion Sort

**Type:** Home Challenge

Problem :

 Minimum Number of Moves to Seat Everyone Given two integer arrays seats and students, both of length n, where seats[i] is the position of the i-th seat and students[i] is the position of the i-th student, return the minimum number of moves required to seat each student in a seat such that no two students occupy the same seat. 

A student can move one position left or right at a cost of 1 move. 

Use insertion sort to sort both arrays in ascending order, then compute the total moves as the sum of absolute differences between corresponding positions (|seats[i] - students[i]|). This problem applies insertion sort to a real-world optimization scenario, like assigning resources in a distributed system (e.g., aligning tasks to nodes in Kubernetes). It challenges students to handle small arrays with duplicates and compute a derived result. Constraints: 

n == seats.length == students.length 

1 ≤ n ≤ 100 

1 ≤ seats[i], students[i] ≤ 100 Example: 

Input: seats = [3,1,5], students = [2,7,4] 

Output: 4 

Explanation: Sort seats = [1,3,5], students = [2,4,7] using insertion sort, then moves = |1-2| + |3-4| + |5-7| = 1 + 1 + 2 = 4. Why It Fits: Requires applying insertion sort twice on small arrays, handling duplicates, and computing a post-sorting metric, pushing students to integrate sorting with optimization logic. 

 

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
