'''
Link: https://leetcode.com/problems/reverse-linked-list/
Level: Easy
Companies: Inuit, Yandex
'''

from hashlib import new


class Node:
    def __init__(self, input):
        self.data = input 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 
    
    def print(self):
        temp = self.head
        while temp != None:                                     #Try while(temp)
            print(temp.data, end=" ")
            temp = temp.next 
        print("")

    def addBefore(self, input):
        new_node = Node(input)
        new_node.next = self.head
        self.head = new_node

    def append(self, input): 
        new_node = Node(input)
        
        if self.head == None: 
            self.head = new_node
            return
        
        tail = self.head 
        while tail.next != None:
            tail = tail.next 
        
        tail.next = new_node

    def insert(self, prevNode, input):
        if prevNode == None:
            print("Previous node not found")
            return 

        new_node = Node(input)
        new_node.next = prevNode.next
        prevNode.next = new_node

    def reverse(self):
        curr = self.head
        prev = None 
        temp = None 
        while curr != None:
            prev = curr
            curr = curr.next
            prev.next = temp 
            temp = prev
        self.head = prev
        return prev


def merge(list1, list2): 
    dummy = Node(0)
    tail = dummy
    while True:
        if list1 == None: 
            tail.next = list2
            break
        elif list2 == None: 
            tail.next = list1
            break 

        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next 
        else: 
            tail.next = list2
            list2 = list2.next 
        tail = tail.next
    return dummy.next



list1 = LinkedList()
list2 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)
list1.print()

list2.append(2)
list2.append(4)
list2.append(6)
list2.print()

list1.head = merge(list1.head, list2.head)
list1.print()


