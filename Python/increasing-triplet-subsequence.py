'''
Link: https://leetcode.com/problems/increasing-triplet-subsequence/
Level: Medium
Companies: Na
https://zhenyu0519.github.io/2020/03/02/lc334/
'''

class Solution:
    def increasingTriplet(self, nums) -> bool:
        first, second = float('inf'), float('inf')
        for i in nums:
            if i <= first: 
                first = i 
            elif i <= second:
                second = i
            else:
                return True
        return False


obj = Solution()
nums1 = [1,2,3,4,5]
nums2 = [5,4,3,2,1]
nums3 = [2,1,5,0,4,6]
print(obj.increasingTriplet(nums1))
print(obj.increasingTriplet(nums2))
print(obj.increasingTriplet(nums3))