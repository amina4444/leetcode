class Solution(object):
    def majorityElement(self, nums):
        count = {}

        for m in nums:
            if m in count:
                count[m] += 1
            else:
                count[m] = 1

            if count[m] > len(nums) // 2:
                return m
        """
        :type nums: List[int]
        :rtype: int
        """
        