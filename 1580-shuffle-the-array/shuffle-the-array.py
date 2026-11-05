class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        length = len(nums)
        left = nums[:n]
        right = nums[n:]
        nums[::2] = left
        nums[1::2] = right
        return nums
        
