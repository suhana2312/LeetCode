class Solution(object):
    def subtractProductAndSum(self, n):
        temp=n
        sum_=0
        product=1
        while temp>0:
            r=temp%10
            temp=temp//10
            sum_=sum_+r
            product=product*r
        return product-sum_    

        