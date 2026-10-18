class Solution(object):
    def intersection(self, nums1, nums2):
        result=[]
        for nums in nums1:
            if nums in nums2 and nums not in result:
                result.append(nums)
        return result        