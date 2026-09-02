class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0]
        preSumL = [0]
        preSumR = [0] 
        answer = [] 
        for i in range(len(nums)-1):
            preSumL.append(preSumL[-1] + nums[i])
            preSumR.append(preSumR[-1] + nums[-(i+1)])
        preSumR.reverse()
        for i in range(len(nums)):
            answer.append(abs(preSumL[i] - preSumR[i]))
        return answer