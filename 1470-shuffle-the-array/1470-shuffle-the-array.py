class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        nums1 = nums[:n]
        nums2 = nums[n:]
        for nums1,nums2 in zip(nums1,nums2):
            res.append(nums1)
            res.append(nums2)
        return res


        