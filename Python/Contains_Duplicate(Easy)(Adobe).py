#https://leetcode.com/problems/contains-duplicate/

'''
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        unique = set()
        for i in nums:
            if i not in unique:
                unique.add(i)
            else: 
                return True
        return False
            

obj = Solution()
nums = [1, 2, 3, 4]
nums = [1, 1, 2, 3, 4]
print(obj.containsDuplicate(nums))