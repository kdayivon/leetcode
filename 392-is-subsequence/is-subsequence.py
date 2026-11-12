class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        i = 0
        for j in range(n):
            if i == len(s):
                return True
            if s[i] == t[j]:
                i += 1
        return i == len(s)