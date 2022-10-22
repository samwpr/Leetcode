class Node:
    def __init__(self, input):
        self.data = input
        self.next = None 


class LinkedList:
    def __init__(self):
        self.head = None 
    
    def addBefore(self, input):
        new_node = Node(input)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prevNode, input):
        if prevNode is None:
            print("there is no previous node")
            return 

        new_node = Node(input)
        new_node.next = prevNode.next
        prevNode.next = new_node

    def append(self, input):
        new_node = Node(input)
        if self.head is None:
            self.head = new_node
            return

        tail = self.head
        while tail.next != None:
            tail = tail.next 
        tail.next = new_node

    def printList(self):
        temp = self.head 
        while temp!= None:
            print(temp.data)
            temp = temp.next
        print("")


list1 = LinkedList()
list1.addBefore(1)
list1.addBefore(2)
list1.addBefore(3)
list1.append(4)
list1.insert(list1.head, 5)
list1.printList()




