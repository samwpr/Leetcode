#https://leetcode.com/problems/two-sum/

def twoSum(nums: list, target: int) -> list:
    numDict = {}
    for index, number in enumerate(nums):
        diff = target - number
        if diff in numDict.keys():
            return [numDict[diff], index]
        numDict[number] = index

print(twoSum([2, 7, 11, 15], 9))

