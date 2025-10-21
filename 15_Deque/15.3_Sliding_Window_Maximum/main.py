# Sliding Window Maximum
# Topic: Deque
# Type: In-Session

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pass

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  
    print(sol.maxSlidingWindow([9,5,3,1,2,8], 2))      
    print(sol.maxSlidingWindow([2,1], 2))               
