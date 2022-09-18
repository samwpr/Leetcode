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
        unique = set()
        for i in nums: 
            if i in unique:
                return True
            else:
                unique.add(i)
        return False

obj = Solution()
nums = [1,2,3,1]
print(obj.containsDuplicate(nums))
nums = [1,2,3,4]
print(obj.containsDuplicate(nums))
nums = [1,1,1,3,3,4,3,2,4,2]
print(obj.containsDuplicate(nums))
