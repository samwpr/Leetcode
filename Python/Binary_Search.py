'''
Link: https://leetcode.com/problems/binary-search/
Level: Easy
Companies: Na
'''
class Solution:
    def search(self, nums, target) -> int:
        left = 0
        right = len(nums) -1
        while left <= right: 
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: 
                left = mid + 1
            else: 
                right = mid - 1
        return -1
        
obj = Solution()
nums = [5]
target = 5
print(obj.search(nums, target))