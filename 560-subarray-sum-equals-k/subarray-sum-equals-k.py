class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt_dict:dict = {0:1}
        total:int = 0
        res:int = 0

        for num in nums:
            total += num
            if (total - k) in cnt_dict:
                res += cnt_dict[total - k]
            cnt_dict[total] = cnt_dict.get(total, 0) + 1
        
        return res

