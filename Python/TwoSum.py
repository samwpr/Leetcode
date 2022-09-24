'''
Link: https://leetcode.com/problems/two-sum/
Level: Easy
Companines: Google, Accenture, Adobe, Amazon, Amex, Apple, Bloomberg, Dell, Expedia, Goldman, IBM, Intel, Intuit, JP, MicroSoft, Morgan Stanley, Orcale, Paypal, Salesforce, Samsung, Spotify, Uber, Visa, Walmart, Yahoo, Zillow, Zoho, Zomato, Zoom
'''

class Solution(object):
    def twoSum(self, nums: list, target: int) -> list:
        dictionary = {}
        for index, element in enumerate(nums):
            diff = target - element
            if diff in dictionary.keys():
                return [dictionary[diff], index]
            else: 
                dictionary[element] = index


obj = Solution()
nums = [2, 7, 11, 15]
target = 9
print(obj.twoSum(nums, target))

