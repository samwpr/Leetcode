from random import randint
from collections import defaultdict

class leetcode(object):
    def __init__(self):
        self.size = -1
        self.problem_id = 0
        self.dict = defaultdict(dict)
    
    def add(self, problem_name: str, problem_url: str): 
        self.dict[self.problem_id][problem_name] = problem_url
        self.problem_id += 1
        self.size += 1

    def generate(self):
        number = randint(0, self.size)
        print("Number of questions:", self.size+1)
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
#database.add(" |  | ", " ")

database.generate()



