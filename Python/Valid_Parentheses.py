'''
Link: https://leetcode.com/problems/valid-parentheses/
Level: Easy
Companies: Adobe, Amazon, Arista Networks, Barclays, Bloomberg, Booking, Cisco, Dataminr, Expedia, Intel, Linkedin, Microsoft, Netflix, Oracle, ServiceNow, Spotify, VMware, Yandex, tcs

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {")":"(", "}":"{", "]":"["}
        stack = []
        for i in s:
            if i in dictionary.values():
                stack.append(i)
            elif stack and dictionary[i] == stack[-1]:
                stack.pop()
            else: 
                return False
        return stack == []

obj = Solution()
#print(obj.isValid("()"))
#print(obj.isValid("()[]{}"))
#print(obj.isValid("(]"))
#print(obj.isValid("([])"))
#print(obj.isValid(")"))
print(obj.isValid("(){}}{"))


'''
()
if ( is a value add to stack 
if ) is not a value check  
dictionary[)] = stack[-1]
return false 

)(





'''