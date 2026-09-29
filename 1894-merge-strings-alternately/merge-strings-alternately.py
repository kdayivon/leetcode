class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first = list(word1)
        sec = list(word2)
        merged = [""] * (len(first) + len(sec))
        i = 0
        j = 0
        k = min(len(first), len(sec))
        while (j < k):
            merged[i] = first[j]
            i += 1
            merged[i] = sec[j]
            i += 1
            j += 1
        
        if (len(first) >= len(sec)):
            while (i < len(merged)):
                merged[i] = first[j]
                i += 1
                j += 1
        else:
            while (i < len(merged)):
                merged[i] = sec[j]
                i += 1
                j += 1
        return "".join(merged) 