class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        sortL = sorted(people)
        left = 0
        right = len(people) - 1
        boats = 0
        while (left <= right): 
            calc = sortL[left] + sortL[right]
            if (calc <= limit):
                left += 1
            boats += 1
            right -= 1
        return boats