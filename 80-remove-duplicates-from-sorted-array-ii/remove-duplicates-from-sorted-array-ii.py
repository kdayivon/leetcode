class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left, right = 0, 0
        count = 0
        k = 1
        while (right < len(nums)):
            if (nums[left] == nums[right]):
                count += 1
                if (count > 2):
                    nums[right] = 10**10
                    k = 2
                right += 1
            else:
                count = 0
                left = right
        nums.sort()
        if (k > 1):
            while (nums[k] != nums[-1]):
                k += 1
        else:
            k = len(nums)
        return k