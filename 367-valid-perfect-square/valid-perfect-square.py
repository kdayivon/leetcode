class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while (left <= right):
            mid = left + (right - left) // 2
            sqr_mid = mid * mid
            if (sqr_mid == num) and (isinstance(mid, int)):
                return True
            elif (sqr_mid < num):
                left = mid + 1
            elif (sqr_mid > num):
                right = mid - 1

        return False
