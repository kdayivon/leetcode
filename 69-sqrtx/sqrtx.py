class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while (left <= right):
            mid = (left + right) // 2
            sqr_mid = mid * mid
            if (sqr_mid == x):
                return mid  
            elif (sqr_mid > x):
                right = mid - 1
            elif (sqr_mid < x):
                left = mid + 1
        return right 
