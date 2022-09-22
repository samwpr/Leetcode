'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Companies: Adobe, Alation, Amazon, Apple, Atlassian, Bloomberg, ByteDance, Capital One, Cisco, Docusign, Expedia, Goldman Sachs, JP Morgan, Netflix, Orcale, Paypal, ServiceNow, Uber, Visa, Walmart, Zoho, Zoom, eBay, tcs
'''

def maxProfit(prices: list) -> int:
    profit = 0 
    index = 0
    for i in range(1, len(prices)):
        if prices[i] < prices[index]:
            index = i
        profit = max(profit, prices[i] - prices[index])
    return profit
    


prices1 = [7,2,10,1,6]
print(maxProfit(prices1))

prices = [7,6,4,3,1]
print(maxProfit(prices))

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
