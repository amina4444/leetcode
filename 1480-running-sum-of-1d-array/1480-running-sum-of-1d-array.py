class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res = []
        n = 0

        for m in nums:
            n += m
            res.append(n)
        return(res)
        