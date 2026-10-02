class Solution(object):
    def sortArrayByParity(self, nums):
        n=len(nums)
        i=0
        for j in range(n):
            if nums[j]%2==0:
                temp=nums[j]
                nums[j]=nums[i]
                nums[i]=temp
                i=i+1
        return nums        