class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        summ = n * (n + 1) // 2
        sum_nums = sum(nums)
        missing_num = summ - sum_nums
        return missing_num
        """
        :type nums: List[int]
        :rtype: int
        """
        