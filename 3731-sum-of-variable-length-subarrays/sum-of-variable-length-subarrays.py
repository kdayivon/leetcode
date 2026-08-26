class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        # compute the sum of the subarray in nums for each i from i..n
        total = 0
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            x = sum(nums[start:i+1])
            total += x
        return total