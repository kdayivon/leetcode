class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # we have to tell the trucks the "addresses" of where to pick up the garbage
        total = 0
        address = {}
        preSum = [0]
        truck = "MPG"

        for i, house in enumerate(garbage):
            address[i] = list(house)

        for i in range(len(travel)):
            preSum.append(preSum[-1] + travel[i])

        for i in range(len(truck)):
            pickup,  timing = 0, 0
            for key, value in address.items():
                if truck[i] in value:
                    timing = preSum[key]
                    pickup += value.count(truck[i])
            print(timing, pickup)
            print("---")
            total += timing + pickup
        return total