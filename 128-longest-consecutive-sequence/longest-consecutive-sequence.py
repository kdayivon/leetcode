class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        n:int = len(nums)
        res:int = 0
        set_nums:set = set(nums)
        
        for n in set_nums:
            if (n - 1) not in set_nums:
                length:int = 1
                while (n + length) in set_nums:
                    length += 1
                res = max(res, length)
                
        return res
