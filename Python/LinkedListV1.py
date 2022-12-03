class Node:
    def __init__ (self, input):
        self.data = input 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 
    
    def addBefore(self, input):
        node = Node(input)
        node.next = self.head 
        self.head = node 

    def append(self, input):
        node = Node(input)
        if self.head == None:
            self.head = node
            return 

        temp = self.head 
        while temp.next != None:
            temp = temp.next 
        temp.next = node 

    def prevNode(self, prev, input):
        if prev == None:
            print("lolzyzz")
            return 

        node = Node(input)
        node.next = prev.next
        prev.next = node 

    def printList(self):
        temp = self.head 
        while temp != None: 
            print(temp.data, end="")
            temp = temp.next
        print("")



list1 = LinkedList()
list1.addBefore(1)
list1.addBefore(2)
list1.addBefore(3)
list1.printList()
print("")
list1.append(4)
list1.prevNode(list1.head, 5)
list1.printList()




