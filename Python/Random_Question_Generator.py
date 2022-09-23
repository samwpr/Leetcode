from random import randint
from collections import defaultdict

class leetcode(object):
    def __init__(self):
        self.size = -1
        self.problem_id = 1
        self.dict = defaultdict(dict)
    
    def add(self, problem_name: str, problem_url: str): 
        self.dict[self.problem_id][problem_name] = problem_url
        self.problem_id += 1
        self.size += 1

    def generate(self):
        number = randint(0, self.size)
        print("Number of questions:", self.size+1, "\n")
        print(number, self.dict[number])
        
database = leetcode()
database.add("Contains Duplicat | Easy | Adobe", "https://leetcode.com/problems/contains-duplicate/")
database.add("First Bad Version | Easy | Google, Cisco", "https://leetcode.com/problems/first-bad-version/")
database.add("Implement a LinkedList", "Na")
database.add("Happy Number | Easy | Google, Paypal", "https://leetcode.com/problems/happy-number/")
database.add("Palindrome Number | Easy | Accenture, Yahoo", "https://leetcode.com/problems/palindrome-number/")
database.add("Snapshot Array | Easy | Google, Rubrik", "https://leetcode.com/problems/snapshot-array/")
database.add("TwoSum | Easy | NA", "https://leetcode.com/problems/two-sum/")
database.add("Valid Anagram | Easy | Affirm, Spotify", "https://leetcode.com/problems/valid-anagram/")
database.add("Valid Palindrome | Easy | Amex, Wayfair, Yandex", "https://leetcode.com/problems/valid-palindrome/")
database.add("Best Time to Buy and Sell Stock | Easy | Adobe, Alation, Amazon, Apple, Atlassian, Bloomberg, ByteDance, Capital One, Cisco, Docusign, Expedia, Goldman Sachs, JP Morgan, Netflix, Orcale, Paypal, ServiceNow, Uber, Visa, Walmart, Zoho, Zoom, eBay, tcs", "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/")
database.add("Valid Parentheses | Easy | Adobe, Amazon, Arista Networks, Barclays, Bloomberg, Booking, Cisco, Dataminr, Expedia, Intel, Linkedin, Microsoft, Netflix, Oracle, ServiceNow, Spotify, VMware, Yandex, tcs", "https://leetcode.com/problems/valid-parentheses/")
database.add("Binary Search | Easy | Na", "https://leetcode.com/problems/binary-search/")
database.add("Reverse LinkedList | Easy | Intuit, Yandex", "https://leetcode.com/problems/reverse-linked-list/")
database.add("Invert Binary Tree | Easy | Na", "https://leetcode.com/problems/invert-binary-tree/")
database.add("Create Binary Tree| Na | Na", "Na")
database.add("Merge Two Sorted List | Easy | Accenture, Adobe, Orcale, Shoppe", "https://leetcode.com/problems/merge-two-sorted-lists/")
#database.add(" |  | ", " ")
#database.add(" |  | ", " ")

database.generate()



