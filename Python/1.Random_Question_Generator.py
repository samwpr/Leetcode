from random import randint
from collections import defaultdict

class leetcode(object):
    def __init__(self):
        self.size = -1
        self.problem_id = 1
        self.dict = defaultdict(dict)
    
    def add(self, problem_name, problem_url): 
        self.dict[self.problem_id][problem_name] = problem_url
        self.problem_id += 1
        self.size += 1

    def generate(self):
        number = randint(0, self.size)
        print("Number of questions:", self.size+1, "\n")
        print(number, self.dict[number])
        
database = leetcode()
#1
database.add("Contains Duplicat | Easy | Adobe", "https://leetcode.com/problems/contains-duplicate/")
#2
database.add("11 Oct - First Bad Version | Easy | Google, Cisco", "https://leetcode.com/problems/first-bad-version/")
#3
database.add("Implement a LinkedList", "Na")
#4
database.add("Happy Number | Easy | Google, Paypal", "https://leetcode.com/problems/happy-number/")
#5
database.add("Palindrome Number | Easy | Accenture, Yahoo", "https://leetcode.com/problems/palindrome-number/")
#6
database.add("11 Oct - Snapshot Array | Easy | Google, Rubrik", "https://leetcode.com/problems/snapshot-array/")
#7
database.add("TwoSum | Easy | Companines: Google, Accenture, Adobe, Amazon, Amex, Apple, Bloomberg, Dell, Expedia, Goldman, IBM, Intel, Intuit, JP, MicroSoft, Morgan Stanley, Orcale, Paypal, Salesforce, Samsung, Spotify, Uber, Visa, Walmart, Yahoo, Zillow, Zoho, Zomato, Zoom", "https://leetcode.com/problems/two-sum/")
#8
database.add("12 Oct - Valid Anagram | Easy | Affirm, Spotify", "https://leetcode.com/problems/valid-anagram/")
#9
database.add("17 Oct - Valid Palindrome | Easy | Amex, Wayfair, Yandex", "https://leetcode.com/problems/valid-palindrome/")
#10
database.add("12 Oct - Best Time to Buy and Sell Stock | Easy | Adobe, Alation, Amazon, Apple, Atlassian, Bloomberg, ByteDance, Capital One, Cisco, Docusign, Expedia, Goldman Sachs, JP Morgan, Netflix, Orcale, Paypal, ServiceNow, Uber, Visa, Walmart, Zoho, Zoom, eBay, tcs", "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/")
#11
database.add("Valid Parentheses | Easy | Adobe, Amazon, Arista Networks, Barclays, Bloomberg, Booking, Cisco, Dataminr, Expedia, Intel, Linkedin, Microsoft, Netflix, Oracle, ServiceNow, Spotify, VMware, Yandex, tcs", "https://leetcode.com/problems/valid-parentheses/")
#12
database.add("Binary Search | Easy | Na", "https://leetcode.com/problems/binary-search/")
#13
database.add("Reverse LinkedList - Iterative | Easy | Intuit, Yandex", "https://leetcode.com/problems/reverse-linked-list/")
#14
database.add("Reverse LinkedList - Recursive | Easy | Intuit, Yandex", "https://leetcode.com/problems/reverse-linked-list/")
#15
database.add("12 Oct - Invert Binary Tree | Easy | Na", "https://leetcode.com/problems/invert-binary-tree/")
#16
database.add("Create Binary Tree| Na | Na", "Na")
#17
database.add("Merge Two Sorted List | Easy | Accenture, Adobe, Orcale, Shoppe", "https://leetcode.com/problems/merge-two-sorted-lists/")
#18
database.add("Has Cycle | Easy | Spotify(4), Visa(3)", "https://leetcode.com/problems/linked-list-cycle/")
#19
database.add("Factorial recursive| Na | Na", "Na")
#20
database.add("14 Oct - Maximum Depth of Binary Tree (Recursive) | Easy | Spotify(4)", "https://leetcode.com/problems/maximum-depth-of-binary-tree/")
#21
database.add("Maximum Depth of Binary Tree (DFS) | Easy | Spotify(4)", "https://leetcode.com/problems/maximum-depth-of-binary-tree/")
#22
database.add("Maximum Depth of Binary Tree (BFS) | Easy | Spotify(4)", "https://leetcode.com/problems/maximum-depth-of-binary-tree/")
#23
database.add("10 Oct - Break a palindrome | Medium | Na", "https://leetcode.com/problems/break-a-palindrome/")
#24
database.add("11 Oct - Increasing Triplet Subsequence | Medium | Na", "https://leetcode.com/problems/increasing-triplet-subsequence/")
#25
database.add("12 Oct - Largest Perimeter Triangle | Easy | Tesla", "https://leetcode.com/problems/largest-perimeter-triangle/")
#26
database.add("12 Oct - Binary Tree In Order Traversal | Easy | Na", "https://leetcode.com/problems/binary-tree-inorder-traversal/")
#27
database.add("Diameter of Binary Tree | Easy | Na", "https://leetcode.com/problems/diameter-of-binary-tree/")
#28
database.add("Delete Node in a Linked List | Medium | Na", "https://leetcode.com/problems/delete-node-in-a-linked-list/")
#29
database.add("Delete Middle Node of a LinkedList | Medium | Na", "https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/")
#30
database.add("17 Oct - Check if sentence is a Pangram | Easy | Na", "https://leetcode.com/problems/check-if-the-sentence-is-pangram/")
#31
database.add("Balanced Binary Tree | Easy | Spotify ", "https://leetcode.com/problems/balanced-binary-tree/")
#32
database.add("Count and say | Medium | Na", "https://leetcode.com/problems/count-and-say/")
#33
database.add("Top K Frequent Words | Medium | Two Sigma(2), Uber(17), Yahoo(4)", "https://leetcode.com/problems/top-k-frequent-words/")
#34
database.add("Integer to Roman | Medium | Capital One(3) ", "https://leetcode.com/problems/integer-to-roman/")
#35
database.add("Same Tree | Easy | Na", "https://leetcode.com/problems/same-tree/")
#3
#database.add(" |  | ", " ")

database.generate()



