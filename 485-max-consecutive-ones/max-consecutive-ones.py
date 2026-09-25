class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        consecutive = 0
        for i in range(len(nums)):
            if (nums[i] == 1):
                count += 1
            else:
                consecutive = max(count, consecutive)
                count = 0
        consecutive = max(count, consecutive)
        return consecutive

