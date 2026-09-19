class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        sortL = sorted(nums)

        for i in range(len(sortL) - 2):
            if (sortL[i] > 0):
                break
            if (i > 0) and (sortL[i] == sortL[i-1]):
                continue

            left = i + 1
            right = len(sortL) - 1

            while (left < right):
                calc = sortL[i] + sortL[left] + sortL[right]
                if (calc == 0):
                    ans.append([sortL[i], sortL[left], sortL[right]])
                    left += 1
                    while left < right and sortL[left] == sortL[left-1]:
                        left += 1
                elif (calc < 0):
                    left += 1
                else:
                    right -= 1

        return ans