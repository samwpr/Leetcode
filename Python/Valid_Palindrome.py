#https://leetcode.com/problems/valid-palindrome/


from curses.ascii import isalpha


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString = ""
        flippedString = ""
        for i in s.lower():
            if i.isalnum() == True:
                cleanString += i
        print(cleanString)
        
        for j in reversed(cleanString):
            flippedString += j
        print(flippedString)

        if cleanString == flippedString:
            return True
        return False
        

obj = Solution()
#print(obj.isPalindrome("A man, a plan, a canal: Panama")) #True
#print(obj.isPalindrome("race a car")) #False
print(obj.isPalindrome("0P"))

'''
var temp 
lowercase 
remove space 
negative range 
'''

