# Shortest Subarray With Sum At Least K
# Topic: Deque
# Type: Home Challenge

from collections import deque
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pass

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestSubarray([2,-1,2], 3))             
    print(sol.shortestSubarray([1,2], 4))                  
    print(sol.shortestSubarray([1,2,3,4,5], 11))          
    print(sol.shortestSubarray([84,-37,32,40,95], 167))   
