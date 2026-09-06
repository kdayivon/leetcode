class Solution:
    def pivotInteger(self, n: int) -> int:
        preSum = [0] * n
        postSum = [0] * n
        postSum[0] = n
        preSum[0] = 1
        for i in range(1, n):
            preSum[i] = preSum[i-1] + (i+1)
            postSum[i] = postSum[i-1] + (n-i)
        for j in range(n):
            try:
                if (preSum[j] in postSum) and (j - (n-1-postSum.index(preSum[j])) == 0):
                    return j+1
            except: 
                continue
        return -1       