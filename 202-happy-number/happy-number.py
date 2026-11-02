class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            n = self.sum_squares(n)
        return False

    def sum_squares(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit *= digit
            output += digit
            n = n // 10
        return output


