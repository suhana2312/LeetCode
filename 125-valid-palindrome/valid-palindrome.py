class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        ans=""
        for i in s:
            if i.isalnum():
                ans+=i
        rev=ans[::-1 ]  
        if ans==rev:
            return True
        else:
            return False         