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

    def append(self, input):
        new_node = Node(input)
        if self.head == None:
            self.head = new_node
            return 

        temp = self.head 
        while temp.next != None:
            temp = temp.next 

        temp.next = new_node

    def insert(self, prevNode, input):
        if prevNode == None:
            print('There is not previous node')
            return 

        new_node = Node(input)
        new_node.next = prevNode.next
        prevNode.next = new_node

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
list1.insert(list1.head, 5)
list1.printList()




