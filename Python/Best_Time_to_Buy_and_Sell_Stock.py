'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Companies: Adobe, Alation, Amazon, Apple, Atlassian, Bloomberg, ByteDance, Capital One, Cisco, Docusign, Expedia, Goldman Sachs, JP Morgan, Netflix, Orcale, Paypal, ServiceNow, Uber, Visa, Walmart, Zoho, Zoom, eBay, tcs
'''

def maxProfit(prices: list) -> int:
    res = 0

    l = 0
    for r in range(1, len(prices)):
        print(prices[r], prices[l])
        if prices[r] < prices[l]:
            l = r
        #print(prices[r], prices[l])
        print("l =", l)
        print("max", prices[r], prices[l])
        res = max(res, prices[r] - prices[l],)
        print("res",res)
    return res


prices1 = [7,2,10,1,6]
print(maxProfit(prices1))

prices = [7,6,4,3,1]
#print(maxProfit(prices))

prices = [7,1,5,3,6,4]
#print(maxProfit(prices))

