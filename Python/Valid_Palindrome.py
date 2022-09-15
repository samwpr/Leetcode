#https://leetcode.com/problems/valid-palindrome/

from audioop import reverse
from curses.ascii import isalpha
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        justAlpha = ""
        for i in s.lower():
            if str.isalnum(i): 
                justAlpha += i
        print(justAlpha)

        reverse = justAlpha[::-1]
        print(reverse)
        if justAlpha == reverse:
            return True
        return False


'''
0. lowercase 
1. Check str.isalpha
2. Remove not alphabetic characters
3. reverse string and compare [::-1]
'''

obj = Solution()
#print(obj.isPalindrome("A man, a plan, a canal: Panama")) #True
#print(obj.isPalindrome("race a car")) #False
#print(obj.isPalindrome(" ")) #True
#print(obj.isPalindrome("0P"))
