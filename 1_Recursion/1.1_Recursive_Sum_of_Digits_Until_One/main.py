# Recursive Sum of Digits Until One
# Topic: Recursion
# Type: In-Session
class Solution:
    def recursiveDigitSum(self, n: int) -> int:
        if n < 10:
            return n

        current_sum = 0
        temp_n = n
        while temp_n > 0:
            current_sum += temp_n % 10
            temp_n //= 10

        return self.recursiveDigitSum(current_sum)
if __name__ == '__main__':
    sol = Solution()
    print(sol.recursiveDigitSum(9875))   
    print(sol.recursiveDigitSum(1234))   
    print(sol.recursiveDigitSum(5))
