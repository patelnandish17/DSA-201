# Largest Rectangle in Histogram
# Topic: Stack
# Type: Home Challenge

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Implement monotonic stack based histogram area calculation
        pass

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.largestRectangleArea([2,1,5,6,2,3]))  
    print(sol.largestRectangleArea([2,4]))          

