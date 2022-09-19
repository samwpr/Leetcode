'''
Link: https://leetcode.com/problems/reverse-linked-list/
Level: Easy
Companies: Inuit, Yandex

TODO: Reverse recursively
'''


import re


class ListNode():
    def __init__(self, input: int, node = None):
        self.data = input
        self.next_node = node 

class LinkedList():
    def __init__(self, rootNode = None):
        self.root = rootNode
        self.size = 0
    
    def add(self, input: int):
        new_node = ListNode(input, self.root)
        self.root = new_node
        self.size += 1

    def print(self):
        temp = self.root
        while temp != None: 
            print(temp.data, end=" ")
            temp = temp.next_node
        print("")

    def reverse_Iterative(self):
        prev = None 
        current = self.root
        while current != None:
            next_node = current.next_node
            current.next_node = prev
            prev = current
            current = next_node
        self.root = prev

    '''
    def reverse_Recurvise(self, rootNode: ListNode):
        if rootNode == None or rootNode.next_node == None:
            return rootNode
        current = self.reverse_Recurvise(rootNode.next_node)
        rootNode.next_node = rootNode
        rootNode.next_node = None
        return current
    '''


obj = LinkedList()
obj.add(1)
obj.add(2)
obj.add(3)
obj.print()
obj.reverse_Iterative()
obj.print()
obj.reverse_Recurvise()
obj.print()



        