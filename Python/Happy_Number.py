class Solution(object):
    #@snoop
    def isHappy(self, n: int) -> bool:
        pastNum = set() #using set as all values need to be unique to ensure no infinite loop
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n not in pastNum:
                pastNum.add(n)
            else: 
                return False
        return True

        
obj = Solution()
print(obj.isHappy(19))
print(obj.isHappy(2))

























