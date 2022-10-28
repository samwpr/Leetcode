'''
Contains Duplicate II

Given an integer array nums and an integer k, return true if there
are two distinct indices i and j in the array such that 
nums[i] == nums[j] and abs(i - j) <= k
'''

class Solution:
    def containsDuplicateTwo(self, nums: list[int], k: int) -> bool:
        dict = {}
        for index, element in enumerate(nums):
            if element in dict and index - dict[element] <= k:
                print("index:", index)
                print("Dict", dict[element])
                return True
            dict[element] = index
        return False

obj = Solution()
print(obj.containsDuplicateTwo([1,2,3,1], k=3)) #Output: True

print(obj.containsDuplicateTwo([1,0,1,1], k=1)) #Output: True

print(obj.containsDuplicateTwo([1,2,3,1,2,3], k=2)) #Output: False




