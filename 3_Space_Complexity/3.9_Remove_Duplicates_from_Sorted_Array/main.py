# Remove Duplicates from Sorted Array
# Topic: Space Complexity
# Type: Home Challenge

class Solution:
    def removeDuplicates(self, arr: list[int]) -> int:
        pass

# Demo
if __name__ == '__main__':
    sol = Solution()
    arr = [1,1,2,2,3]
    length = sol.removeDuplicates(arr)
    print(length)                        # Output: 3
    print(arr[:length])                   # Output: [1,2,3]

