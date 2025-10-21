# Subarray Sum Equals K with Length Constraints
# Topic: Hashtables
# Type: Home Challenge

from typing import List

class Solution:
    def subarraySumLengthConstrained(self, nums: List[int], k: int, m: int, n: int) -> int:
        pass

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySumLengthConstrained([1,1,1], 2, 2, 2))        
    print(sol.subarraySumLengthConstrained([1,2,3,1], 3, 1, 2))        
    print(sol.subarraySumLengthConstrained([2,2,2,2], 4, 2, 3))        
    print(sol.subarraySumLengthConstrained([1,-1,1,-1], 0, 2, 4))      
