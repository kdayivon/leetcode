class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_first(nums, target):
            n = len(nums)
            left, right = 0, n - 1
            first= -1
            while (left <= right):
                mid = left + (right - left) // 2
                if (nums[mid] == target):
                    first = mid
                    right = mid - 1
                elif (nums[mid] < target):
                    left = mid + 1
                elif (nums[mid] > target):
                    right = mid - 1
            return first

        def find_last(nums, target):
            n = len(nums)
            left, right = 0, n - 1
            last= -1
            while (left <= right):
                mid = left + (right - left) // 2
                if (nums[mid] == target):
                    last = mid
                    left = mid + 1
                elif (nums[mid] < target):
                    left = mid + 1
                elif (nums[mid] > target):
                    right = mid - 1
            return last
        first = find_first(nums, target)
        last = find_last(nums, target)
        return [first, last]