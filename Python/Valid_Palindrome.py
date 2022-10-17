#https://leetcode.com/problems/valid-palindrome/


from curses.ascii import isalpha


class Solution:
    def isPalindrome(self, s: str):
        clean = ""
        for i in s:
            if i.isalnum() == True:
                clean += i
        
        reverse = clean[::-1]
        reverse = reverse.lower()
        clean = clean.lower()
        print(clean)
        print(reverse)
        
        if reverse == clean:
            return True
        else:
            return False 


obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama")) #True
#print(obj.isPalindrome("race a car")) #False
#print(obj.isPalindrome("0P"))

'''
var temp 
lowercase 
remove space 
negative range 
'''

