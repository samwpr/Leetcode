#https://leetcode.com/problems/valid-anagram/

'''
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false

Constraints:
s and t consist of lowercase English letters.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(t) != len(s):
            return False

        sList = []
        for i in s:
            sList.append(i)
        for j in t: 
            if j in sList:
                sList.remove(j)
            else: 
                return False
        return True
        



obj = Solution()
s = "anagram"
t = "nagaram"

s = "rat"
t = "car"
print(obj.isAnagram(s, t))