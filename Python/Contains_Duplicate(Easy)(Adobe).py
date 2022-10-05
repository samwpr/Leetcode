#https://leetcode.com/problems/contains-duplicate/
#Easy | Adobe

'''
Input: nums = [1,2,3,1]
Output: true

Input: c
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        unqiue = set()
        for i in nums: 
            if i in unqiue:
                return True 
            else:
                unqiue.add(i)
        return False

obj = Solution()
nums = [1,2,3,1]
print(obj.containsDuplicate(nums))

