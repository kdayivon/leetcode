class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i, char in enumerate(s):
            seen[char] = seen.get(char, 0) + 1
        for i in range(len(s)):
            if (seen[s[i]] == 1):
                return i 
        return -1



