# Delivering Boxes from Storage to Ports
**Topic:** Queue

**Type:** Home Challenge

Problem :

You need to deliver boxes from storage to ports using a ship. The ship has limits on both the maximum number of boxes it can carry (maxBoxes) and the total weight it can carry (maxWeight). Boxes must be delivered in the order they appear. Each box is represented as [port, weight]. 

You want to minimize the total number of ship trips made. Each trip consists of: 

Loading consecutive boxes respecting maxBoxes and maxWeight. 

Delivering boxes in the order loaded. Switching ports counts as new trip segments. 

A return trip from last port to storage. 

Examples: 

Input: 

boxes = [[1,2],[1,2],[2,1],[2,1]] 
 portsCount = 2 
 maxBoxes = 3 
 maxWeight = 3 
  
 

Output: Minimum number of trips = 4 
 Explanation: Delivered boxes in two shipments to minimize trips while respecting constraints. 

Input: 

boxes = [[1,2],[2,4],[1,1],[2,1],[3,2]] 
 portsCount = 3 
 maxBoxes = 3 
 maxWeight = 6 
  
Output: 6 


Input: 

boxes = [[1,1]] 
 portsCount = 1 
 maxBoxes = 1 
 maxWeight = 1 
  

Output: 2 

Input: 

boxes = [[1,2],[1,2],[1,2]] 
 portsCount = 1 
 maxBoxes = 3 
 maxWeight = 6 

Output: 3 

Constraints: 

Number of boxes up to 10^5. 

1 <= portsCount, maxBoxes, maxWeight <= 10^5. 

Boxes must be delivered in order. 

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
