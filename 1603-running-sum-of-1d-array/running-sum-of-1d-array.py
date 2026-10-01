class Solution(object):
    def runningSum(self, nums):
        n=len(nums)
        list=[]
        list.append(nums[0])
        for i in range(1,n):
            a=list[i-1]+nums[i]
            list.append(a)
        return list    