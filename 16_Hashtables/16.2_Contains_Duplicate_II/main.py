# Contains Duplicate II
# Topic: Hashtables
# Type: Home Challenge

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pass

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyDuplicate([1,2,3,1], 3))      
    print(sol.containsNearbyDuplicate([1,0,1,1], 1))       
    print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2))    
    print(sol.containsNearbyDuplicate([], 0))              
