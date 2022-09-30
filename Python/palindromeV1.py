'''
Link: https://leetcode.com/problems/palindrome-number/
Level: Easy
Companies: Accenture, Yahoo
'''

class palindrome(object):
    def calculate(self, num: int) -> bool:
        if num < 0:
            return False

        temp = num
        reversed = 0
        while temp != 0: 
            reversed = reversed * 10 + (temp % 10)
            temp = temp // 10

        if reversed == num:
            return True
        return False




obj = palindrome()
print(obj.calculate(121)) #true
print(obj.calculate(-121)) #false
print(obj.calculate(10)) #false


'''
temp 
temp compare with num 
I temp to be reversed num 
121 % 10 = 1 

while temp is not 0 
temp = 121 
x = 121 % 10 = 1 
reversed = 0 
reversed = reversed * 10 + x 
reversed = reversed * 10 + 1 
reversed = 1 

x = 121 // 10 = 12 

12 % 10 = 2 

reversed = 1 * 10 + 2
reversed = 12

x = 12 // 10
1 
'''




