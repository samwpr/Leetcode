class palindrome(object):
    def calculate(self, num: int) -> bool:
        if num < 0: return False

        reversed = 0
        temp = num
        while temp != 0:
            i = temp % 10 
            reversed = reversed * 10 + i
            temp //= 10 
        
        if reversed == num: return True
        else: return False


palindrome = palindrome()  
print(palindrome.calculate(123))

            
         






