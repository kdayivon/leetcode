class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = [0] * (2*len(nums))
        k = len(nums)
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[k] = nums[i]
            k += 1
        return ans