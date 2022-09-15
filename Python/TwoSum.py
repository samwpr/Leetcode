#https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums: list, target: int) -> list:
        numDict = {}
        for index, element in enumerate(nums):
            diff = target - element
            if diff in numDict.keys():
                return [numDict[diff], index]
            numDict[element] = index

obj = Solution()
nums = [2, 7 ,11, 15]
target = 9
print(obj.twoSum(nums, target))


