class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        rSum, lSum, count = 0, sum(nums), 0
        for i in range(len(nums)-1):
            rSum += nums[i]
            lSum -= nums[i]
            if ((rSum - lSum) % 2 == 0):
                count += 1
        return count
