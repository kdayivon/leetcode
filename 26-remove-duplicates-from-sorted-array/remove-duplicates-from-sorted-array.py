class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow, count = 0, 0
        for fast in range(len(nums)):
            if (nums[fast] != nums[slow]):
                slow += 1
                nums[slow] = nums[fast]
        for i in range(len(nums) - 1):
            if (nums[i] < nums[i + 1]):
                count += 1
            else:
                break
        return count + 1
        