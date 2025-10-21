# Min Stack
**Topic:** Stack

**Type:** In-Session

Problem :

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- `push(val)`: Pushes element val onto the stack.  
- `pop()`: Removes the element on the top of the stack.  
- `top()`: Gets the top element of the stack.  
- `getMin()`: Retrieves the minimum element in the stack.

Constraints:
- Operations are valid.  
- At most 3 × 10⁴ calls will be made.

Examples:

| Operation  | Input | Output | Explanation |
|-------------|--------|---------|--------------|
| MinStack()  |        | null    | Initialize stack |
| push        | -2     | null    | Stack: [-2] |
| push        | 0      | null    | Stack: [-2, 0] |
| push        | -3     | null    | Stack: [-2, 0, -3] |
| getMin      |        | -3      | Minimum is -3 |
| pop         |        | null    | Removes top (-3); Stack: [-2, 0] |
| top         |        | 0       | Top element is 0 |
| getMin      |        | -2      | New minimum is -2 |
| push        | 1      | null    | Stack: [-2, 0, 1] |
| getMin      |        | -2      | Minimum remains -2 |

***


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
