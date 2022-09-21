from audioop import add


class Node:
    def __init__(self, input: int, node = None):
        self.data = input 
        self.next = node 

class SinglyLinkedList:
    def __init__(self, root_node = None):
        self.head = root_node
        self.size = 0 

    def add(self, input: int): 
        new_node = Node(input, self.head)
        self.head = new_node 
        self.size += 1 

    def print(self):
        temp_node = self.head 
        while temp_node != None: 
            print(temp_node.data, end="")
            temp_node = temp_node.next 
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




myList = SinglyLinkedList()
myLis2 = SinglyLinkedList()
myList.add(1)
myList.add(2)
myList.add(3)
myList.print()
myList.reverse()
myList.print()

