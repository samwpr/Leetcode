from curses.panel import new_panel


class Node:
    def __init__(self, input):
        self.next = None 
        self.data = input

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printRoot(self):
        print(self.data)

    def printList(self):
        tail = self.head
        while tail != None:
            print(tail.data, end=" ")
            tail = tail.next
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
            print("There is no previous node")
            return 

        new_node = Node(input)
        new_node.next = prevNode.next
        prevNode.next = new_node


list1 = LinkedList()
list1.addBefore(1)
list1.addBefore(2)
list1.append(3)
list1.printList()

list2 = LinkedList()
list2.append(1)
list2.append(2)
list2.insert(list2.head, 3)
list2.printList()



