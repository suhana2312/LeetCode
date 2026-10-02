class Solution(object):
    def removeDuplicates(self, nums):
        n=len(nums)
        if n<=2:
            return n
        i=1
        for j in range(2,n):
            if nums[j]!=nums[i-1]:
                i=i+1
                nums[i]=nums[j]
        return i+1        

      