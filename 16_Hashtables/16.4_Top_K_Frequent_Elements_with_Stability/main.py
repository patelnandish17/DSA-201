# Top K Frequent Elements with Stability
# Topic: Hashtables
# Type: Home Challenge

from typing import List
from collections import Counter

class Solution:
    def topKFrequentStable(self, nums: List[int], k: int) -> List[int]:
        pass

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequentStable([1,1,1,2,2,3], 2))      
    print(sol.topKFrequentStable([4,4,1,1,2,2], 3))    
    print(sol.topKFrequentStable([3,3,3,2,2,2,1,1], 2))   
    print(sol.topKFrequentStable([5], 1))                
