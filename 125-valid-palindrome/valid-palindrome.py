class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = [ch.lower() for ch in s if ch.isalnum()]
        left = 0
        right = len(k) - 1
        while (left < right):
            if k[left] != k[right]:
                return False
            left += 1
            right -= 1
        return True