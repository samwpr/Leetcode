class Solution:
    #@snoop
    def isHappy(self, n: int) -> bool:
        past = set() 
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n in past:
                return False
            past.add(n)
        return True


        

test1 = Solution()
print(test1.isHappy(19))
print(test1.isHappy2(19))


