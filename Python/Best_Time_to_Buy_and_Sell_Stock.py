'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Companies: Adobe, Alation, Amazon, Apple, Atlassian, Bloomberg, ByteDance, Capital One, Cisco, Docusign, Expedia, Goldman Sachs, JP Morgan, Netflix, Orcale, Paypal, ServiceNow, Uber, Visa, Walmart, Zoho, Zoom, eBay, tcs


class Solution:
    def maxProfit(self, prices: list) -> int:
        smallest = None
        smallestIndex = None

        for index, element in enumerate(prices):
            if smallest is None and smallestIndex is None:
                smallest = element
                smallestIndex = index
            elif element <= smallest:
                smallest = element
                smallestIndex = index
        #print(smallest, smallestIndex)

        maxProfit = None
        maxProfitIndex = None

        for index, element in enumerate(prices[smallestIndex:]):
            temp = element - smallest
            if maxProfit is None: 
                maxProfit = temp
                maxProfitIndex = index
            elif temp > maxProfit:
                maxProfit = temp
                maxProfitIndex = index
        #print(maxProfit, maxProfitIndex)

    def maxProfit2(self, prices: list) -> int:
        prices2 = prices.reverse()

        print(prices2)





obj = Solution()
prices = [7,1,5,3,6,4]
print(obj.maxProfit2(prices))

prices = [7,6,4,3,1]
print(obj.maxProfit2(prices))

prices = [7, 2, 10, 1, 6]
print(obj.maxProfit2(prices))



loop thru array and find smallest 
loop thru array and find biggest 
if biggest is after smallest minus and return z
else remove biggest and find new biggest 
if array only left with smallest return zero 
'''

















def maxProfit(prices: list) -> int:
    List = []

    maxProfit = 0

    for i in reversed(prices):
        List.append(i)
    
    for index, element in enumerate(List):
        startPoint = index
        #print("i ----- ", element)
        for j in List[startPoint+1:]:
            result = element - j
            if result > maxProfit:
                maxProfit = result
    return maxProfit







prices = [7,2,10,1,6]
print(maxProfit(prices))

prices = [7,6,4,3,1]
print(maxProfit(prices))


prices = [7,1,5,3,6,4]
print(maxProfit(prices))