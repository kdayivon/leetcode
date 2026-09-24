class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        n = len(height) - 1
        area = 0
        while (left < right):
            if (height[left] < height[right]):
                area = max(area, height[left] * n)
                left += 1
            elif (height[left] >= height[right]):
                area = max(area, height[right] * n)
                right -= 1
            n -= 1
        return area
            