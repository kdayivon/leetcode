class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        for i in range(2, n):
            sub = s[i-2:i+1]
            if (len(set(sub)) < 3):
                continue
            else:
                cnt += 1
        return cnt
