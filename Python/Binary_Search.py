'''
Link: https://leetcode.com/problems/binary-search/
Level: Easy
Companies: Na
'''

class Solution:
    def search(self, nums: list, target: int) -> int:
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid-1
        return -1


nums = [-1,0,3,5,9,12]
target = 9
obj = Solution()
print(obj.search(nums, target))

nums = [-1,0,3,5,9,12]
target = 2
obj = Solution()
print(obj.search(nums, target))

