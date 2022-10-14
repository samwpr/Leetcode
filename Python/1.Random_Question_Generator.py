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
database.add("11 Oct - First Bad Version | Easy | Google, Cisco", "https://leetcode.com/problems/first-bad-version/")
database.add("Implement a LinkedList", "Na")
database.add("Happy Number | Easy | Google, Paypal", "https://leetcode.com/problems/happy-number/")
database.add("Palindrome Number | Easy | Accenture, Yahoo", "https://leetcode.com/problems/palindrome-number/")
database.add("11 Oct - Snapshot Array | Easy | Google, Rubrik", "https://leetcode.com/problems/snapshot-array/")
database.add("TwoSum | Easy | Companines: Google, Accenture, Adobe, Amazon, Amex, Apple, Bloomberg, Dell, Expedia, Goldman, IBM, Intel, Intuit, JP, MicroSoft, Morgan Stanley, Orcale, Paypal, Salesforce, Samsung, Spotify, Uber, Visa, Walmart, Yahoo, Zillow, Zoho, Zomato, Zoom", "https://leetcode.com/problems/two-sum/")
database.add("12 Oct - Valid Anagram | Easy | Affirm, Spotify", "https://leetcode.com/problems/valid-anagram/")
database.add("Valid Palindrome | Easy | Amex, Wayfair, Yandex", "https://leetcode.com/problems/valid-palindrome/")
database.add("12 Oct - Best Time to Buy and Sell Stock | Easy | Adobe, Alation, Amazon, Apple, Atlassian, Bloomberg, ByteDance, Capital One, Cisco, Docusign, Expedia, Goldman Sachs, JP Morgan, Netflix, Orcale, Paypal, ServiceNow, Uber, Visa, Walmart, Zoho, Zoom, eBay, tcs", "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/")
database.add("Valid Parentheses | Easy | Adobe, Amazon, Arista Networks, Barclays, Bloomberg, Booking, Cisco, Dataminr, Expedia, Intel, Linkedin, Microsoft, Netflix, Oracle, ServiceNow, Spotify, VMware, Yandex, tcs", "https://leetcode.com/problems/valid-parentheses/")
database.add("Binary Search | Easy | Na", "https://leetcode.com/problems/binary-search/")
database.add("Reverse LinkedList - Iterative | Easy | Intuit, Yandex", "https://leetcode.com/problems/reverse-linked-list/")
database.add("Reverse LinkedList - Recursive | Easy | Intuit, Yandex", "https://leetcode.com/problems/reverse-linked-list/")
database.add("12 Oct - Invert Binary Tree | Easy | Na", "https://leetcode.com/problems/invert-binary-tree/")
database.add("Create Binary Tree| Na | Na", "Na")
database.add("Merge Two Sorted List | Easy | Accenture, Adobe, Orcale, Shoppe", "https://leetcode.com/problems/merge-two-sorted-lists/")
database.add("Has Cycle | Easy | Spotify(4), Visa(3)", "https://leetcode.com/problems/linked-list-cycle/")
database.add("Factorial recursive| Na | Na", "Na")
database.add("14 Oct - Maximum Depth of Binary Tree (Recursive) | Easy | Spotify(4)", "https://leetcode.com/problems/maximum-depth-of-binary-tree/")
database.add("Maximum Depth of Binary Tree (DFS) | Easy | Spotify(4)", "https://leetcode.com/problems/maximum-depth-of-binary-tree/")
database.add("Maximum Depth of Binary Tree (BFS) | Easy | Spotify(4)", "https://leetcode.com/problems/maximum-depth-of-binary-tree/")
database.add("10 Oct - Break a palindrome | Medium | Na", "https://leetcode.com/problems/break-a-palindrome/")
database.add("11 Oct - Increasing Triplet Subsequence | Medium | Na", "https://leetcode.com/problems/increasing-triplet-subsequence/")
database.add("12 Oct - Largest Perimeter Triangle | Easy | Tesla", "https://leetcode.com/problems/largest-perimeter-triangle/")
database.add("12 Oct - Binary Tree In Order Traversal | Easy | Na", "https://leetcode.com/problems/binary-tree-inorder-traversal/")
database.add("Diameter of Binary Tree | Easy | Na", "https://leetcode.com/problems/diameter-of-binary-tree/")
database.add("Delete Node in a Linked List | Medium | Na", "https://leetcode.com/problems/delete-node-in-a-linked-list/")
database.add("Delete Middle Node of a LinkedList | Medium | Na", "https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/")
#database.add(" |  | ", " ")

database.generate()



