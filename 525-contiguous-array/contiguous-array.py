class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # using cumulative sum where we replace the 0s with -1 to get a final sum = 0
        # [0,1,1,1,1,1,0,0,0]
        # [-1,0,1,2,3,4,3,2,1]
        seen = {0: -1}       # hashset to find max length between same sum
        currSum = 0     # current prefix sum
        maxLen = 0      # max length between same sum
        for i, num in enumerate(nums):
            currSum += -1 if num == 0 else 1

            if currSum in seen: # if seen, find the max between current maxLen and the distance from first seen occurence (i - previousIndex)
                maxLen = max(maxLen, i - seen[currSum])
            else:   # if not seen, put currSum in seen
                seen[currSum] = i

        return maxLen