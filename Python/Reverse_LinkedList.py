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
        print(input, new_node)
        self.root = new_node
        self.size += 1

    def print(self):
        temp = self.root
        while temp != None: 
            print(temp.data, end=" ")
            temp = temp.next_node
        print("")


    def reverse(self):
        a = self.root
        b = None #This is not needed to declare 
        c = None 

        while a != None: 
            b = a
            a = a.next_node
            b.next_node = c
            c = b 
        self.root = b

        


    def reverse_Iterative(self):
        prev = None
        current = self.root
        print("current = self.root", current, "\n")
        
        while current != None:
            #print("current =", current)
            next_node = current.next_node
            print("next node = current.next_node", current.next_node, "\n")

            current.next_node = prev
            print("current.next_node = prev", current.next_node, prev, "\n")

            prev = current
            print("prev = current", prev, current, "\n")

            current = next_node
            print("current = next_node", current, next_node, "\n")

        self.root = prev
        print("self.root = prev", self.root, prev)



'''
    def reverse_Iterative(self):
        prev = None
        current = self.root
        print("current = self.root", current, "\n")
     
        while current != None:
            #print("current =", current)
            next_node = current.next_node
            print("next node = current.next_node", current.next_node, "\n")

            current.next_node = prev
            print("current.next_node = prev", current.next_node, prev, "\n")

            prev = current
            print("prev = current", prev, current, "\n")

            current = next_node
            print("current = next_node", current, next_node, "\n")

        self.root = prev
        print("self.root = prev", self.root, prev)






    def reverse_Recurvise(self, rootNode: ListNode):
        if rootNode == None or rootNode.next_node == None:
            return rootNode
        current = self.reverse_Recurvise(rootNode.next_node)
        rootNode.next_node = rootNode
        rootNode.next_node = None
        return current
    '''

obj = LinkedList()
obj.add(5)
#obj.print()
obj.add(8)
obj.print()
#print("")
#obj.add(3)
#obj.print()
#obj.reverse_Iterative()
obj.reverse()
obj.print()
#obj.reverse_Recurvise()
#obj.print()



        