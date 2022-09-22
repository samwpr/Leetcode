'''
Link: https://leetcode.com/problems/reverse-linked-list/
Level: Easy
Companies: Inuit, Yandex

TODO: Reverse recursively
'''

class Node:
    def __init__(self, input: int, node = None):
        self.data = input
        self.next = node 

class LinkedList:
    def __init__(self, root = None):
        self.head = root
        self.size = 0

    def add(self, input: int):
        new_node = Node(input, self.head)
        self.head = new_node
        self.size += 1

    def print(self): 
        temp = self.head
        while temp != None: 
            print(temp.data, end="")
            temp = temp.next
        print("")

    def reverse(self):
        a = self.head
        b = None
        c = None
        while a != None: 
            b = a 
            a = a.next
            b.next = c 
            c = b 
        self.head = b


myList = LinkedList()
myList.add(1)
myList.add(2)
myList.add(3)
myList.print()
myList.reverse()
myList.print()
