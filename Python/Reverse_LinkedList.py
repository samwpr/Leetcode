'''
Link: https://leetcode.com/problems/reverse-linked-list/
Level: Easy
Companies: Inuit, Yandex

TODO: Reverse recursively
'''

from audioop import add


class Node:
    def __init__(self, value, node = None):
        self.value = value 
        self.next = node 


class LinkedList:
    def __init__(self, head = None):
        self.head = head 
        self.size = 0
    
    def add(self, value): 
        new_node = Node(value, self.head)
        self.head = new_node
        self.size += 1

    def printList(self):
        temp = self.head
        while temp != None: 
            print(temp.value, end="")
            temp = temp.next 
        print("")

    def reverse(self):
        curr = self.head
        temp = None 
        while curr != None: 
            prev = curr
            curr = curr.next
            prev.next = temp
            temp = prev
        self.head = prev
        return prev
            


myList = LinkedList()
myList.add(1)
myList.add(2)
myList.add(3)
myList.printList()
myList.reverse()
myList.printList()
