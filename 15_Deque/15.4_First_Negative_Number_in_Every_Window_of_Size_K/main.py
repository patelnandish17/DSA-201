# First Negative Number in Every Window of Size K
# Topic: Deque
# Type: Home Challenge

from collections import deque
from typing import List

class Solution:
    def firstNegativeInWindow(self, nums: List[int], k: int) -> List[int]:
        pass
# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.firstNegativeInWindow([12,-1,-7,8,-15,30,16,28], 3))  
    print(sol.firstNegativeInWindow([1,2,3,4], 2))                 
    print(sol.firstNegativeInWindow([-5,2,-3,1,4], 2))            