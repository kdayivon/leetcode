class NumArray:

    def __init__(self, nums: List[int]):
        # given immutable list, pre-process list and compute cumulative sum on instanciation
        # no need for check since constraints 
        self.preSum = [0]   # begin with 0
        for num in nums:    # go through given nums
            self.preSum.append(self.preSum[-1] + num)  # take the last number in preSum and add current number from nums

    def sumRange(self, left: int, right: int) -> int:
        # return the sum from [left..right] from the pre-processed list
        return self.preSum[right+1] - self.preSum[left] # sumList[right] - sumList[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)