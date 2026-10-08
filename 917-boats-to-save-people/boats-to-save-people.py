class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        sortL = sorted(people)
        left = 0
        right = len(people) - 1
        boats = 0
        while (left < right): 
            calc = sortL[left] + sortL[right]
            if (calc > limit):
                boats += 1
                right -= 1
            else:
                boats += 1
                left += 1
                right -= 1
        if (left == right):
            boats += 1
        return boats