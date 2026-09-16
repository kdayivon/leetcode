class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        stringList = list(s)
        i = k-1
        for j in range(k // 2):
            temp = stringList[j]
            stringList[j] = stringList[i]
            stringList[i] = temp
            i -= 1
        return "".join(stringList)