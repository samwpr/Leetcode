'''
Link: https://leetcode.com/problems/happy-number/
Level: Easy
Companies: Google, Paypal
'''

class Solution(object):
    #@snoop
    def isHappy(self, n: int) -> bool:
        res = set()
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n in res:
                return False
            else: 
                res.add(n)
        return True

obj = Solution()
print(obj.isHappy(19))
print(obj.isHappy(2))


























