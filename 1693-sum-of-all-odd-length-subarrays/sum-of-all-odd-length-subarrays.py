class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        def sliding_win(arr, currIndex):
            windowSum = 0
            total = 0
            for idx in range(currIndex):
                windowSum += arr[idx]
            total += windowSum
            for k in range(currIndex, len(arr)):
                windowSum += arr[k] - arr[k - currIndex]
                total += windowSum
            return total

        total = sum(arr)
        if len(arr) < 3:
            return total

        for i in range(3, len(arr) + 1):
            if i % 2 != 0:
                if i < len(arr):
                    total += sliding_win(arr, i)
                else:
                    total += sum(arr)
                    return total 
        return total

