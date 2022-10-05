
'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Companies: Adobe, Alation, Amazon, Apple, Atlassian, Bloomberg, ByteDance, Capital One, Cisco, Docusign, Expedia, Goldman Sachs, JP Morgan, Netflix, Orcale, Paypal, ServiceNow, Uber, Visa, Walmart, Zoho, Zoom, eBay, tcs
prices = [7, 1, 5, 3, 6, 4] #Return 5 as maxProfit
'''

def maxProfit(prices: list) -> int:
    minPrice = prices[0]
    maxProfit = 0
    for i in range(0, len(prices)): 
        if prices[i] < minPrice:
            minPrice = prices[i]
        
        maxProfit = max(maxProfit, prices[i] - minPrice)
    return maxProfit

prices = [7, 1, 5, 3, 6, 4] #Return 5 as maxProfit
print(maxProfit(prices))
