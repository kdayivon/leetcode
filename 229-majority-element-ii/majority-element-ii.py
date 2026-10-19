class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        count_dict = {}
        res = []
        for i, num in enumerate(nums):
            count_dict[num] = count_dict.get(num, 0) + 1
        for key, val in count_dict.items():
            if (val > (n // 3)):
                res.append(key)
        return res 
