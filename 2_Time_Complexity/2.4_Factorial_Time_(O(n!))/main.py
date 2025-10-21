# Factorial Time (O(n!))
# Topic: Time & Space Complexity
# Type: In-Session

from itertools import permutations

class Solution:
    def allPermutations(self, s: str) -> list[str]:
        pass

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.allPermutations("abc"))  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(sol.allPermutations("ab"))   # Output: ['ab', 'ba']
    print(sol.allPermutations("a"))    # Output: ['a']

