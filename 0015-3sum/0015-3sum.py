class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            le = i + 1
            ri = len(nums) - 1

            while le < ri:
                total = nums[i] + nums[le] + nums[ri] 

                if total == 0:
                    res.append([nums[i], nums[le], nums[ri]])

                    le += 1
                    ri -= 1

                    while le < ri and nums[le] == nums[le - 1]:
                        le += 1
                    while le < ri and nums[ri] == nums[ri + 1]:
                        ri -= 1
                
                elif total < 0:
                    le += 1

                else:
                    ri -= 1
            
        return res


                

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        