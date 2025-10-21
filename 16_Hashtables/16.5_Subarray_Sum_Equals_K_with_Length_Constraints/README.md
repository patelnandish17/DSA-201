# Subarray Sum Equals K with Length Constraints
**Topic:** Hashtables

**Type:** Home Challenge


**Problem**

Given an array of integers nums, an integer k, and two integers m and n representing minimum and maximum subarray length respectively, find the total number of continuous subarrays whose sum equals k and whose length is between m and n (inclusive). 

Return the count of such subarrays. 

This problem requires a more refined approach than the original as it adds size constraints, making the prefix sum and hashing approach more complex. 

Examples 

Input: nums = [1][1][1], k = 2, m = 2, n = 2 

Output: 2 

Explanation: Subarrays [1][1] starting at indices 0 and 1 each have sum 2 and length 2. 

Input: nums = [1][2][3][1], k = 3, m = 1, n = 2 

Output: 2 

Explanation: Valid subarrays are [3] with length 1, and [1][2] with length 2. 

Input: nums = [2][2][2][2], k = 4, m = 2, n = 3 

Output: 3 

Explanation: Subarrays [2][2] (indices 0-1, 1-2, 2-3). 

Input: nums = [1, -1, 1, -1], k = 0, m = 2, n = 4 

Output: 4 

Explanation: Subarrays [1, -1], [-1, 1], [1, -1], and [1, -1, 1, -1] meet the criteria. 

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
