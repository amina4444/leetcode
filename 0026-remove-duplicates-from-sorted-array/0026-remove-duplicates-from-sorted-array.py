class Solution(object):
    def removeDuplicates(self, nums):
        set_nums = set(nums)
        nums[:] = sorted(set_nums)
        k = len(nums)
        return k



        