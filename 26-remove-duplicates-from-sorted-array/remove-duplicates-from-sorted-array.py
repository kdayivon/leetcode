class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        seen = set()
        write = 0
        for read in range(n):
            if nums[read] not in seen:
                seen.add(nums[read])
                if write != read:
                    nums[write], nums[read] = nums[read], nums[write]
                write += 1
        return write