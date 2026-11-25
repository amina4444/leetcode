class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        gratest = max(candies)
        result = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= gratest:
                result.append(True)
            else:
                result.append(False)
        return result

                
        