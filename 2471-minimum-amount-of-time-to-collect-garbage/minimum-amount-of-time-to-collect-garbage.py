class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # we have to tell the trucks the "addresses" of where to pick up the garbage
        total = 0
        address = {}
        pickup = {}
        truck = "MPG"
        preSum = [0]

        for i in range(len(travel)):
            preSum.append(preSum[-1] + travel[i])

        for i in range(len(garbage)):
            for c in garbage[i]:
                address[c] = i
                pickup[c] = pickup.get(c, 0) + 1
        for t in truck:
            if t in pickup:
                total += preSum[address[t]] + pickup[t]
        return total
       