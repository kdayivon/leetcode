class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        preSum = []
        ans = [0] * len(boxes)

        for i in range(len(boxes)):
            if int(boxes[i]): 
                preSum.append(i)
        for i in range(len(ans)):
            temp = 0
            for num in preSum:         
                temp += abs(i - num)
            ans[i] = temp 
        return ans
