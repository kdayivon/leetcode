class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        preSum = [0] * (len(gain) + 1)
        for i in range(1, len(gain)+1):
            preSum[i] = preSum[i-1] + gain[i-1]
        return max(preSum)