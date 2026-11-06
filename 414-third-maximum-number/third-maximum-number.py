class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        n = len(nums)
        nums_set = set(nums)

        if len(nums_set) <= 2:
            return max(nums_set)
        elif len(nums_set) == 3:
            return min(nums)

        for _ in range(3):
            ans = max(nums_set)
            nums_set.discard(ans)
        return ans
