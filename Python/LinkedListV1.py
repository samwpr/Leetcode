class ListNode:
    def __init__(self, input):
        self.data = input 
        self.next = None 


class LinkedList:
    def __init__(self):
        self.head = None 
    
    def printlist(self):
        temp = self.head
        while temp != None:
            print(temp.data, end="")
            temp = temp.next 
        print("")

    def addBefore(self, input):
        new_node = ListNode(input)
        new_node.next = self.head
        self.head = new_node

    def append(self, input):
        new_node = ListNode(input)
        if self.head == None:
            self.head = new_node
            return

        temp = self.head
        while temp.next != None:
            temp = temp.next
        
        temp.next = new_node
    
    def insert(self, prev, input):
        if prev == None:
            print("There is no previous node")
            return 

        new_node = ListNode(input)
        new_node.next = prev.next
        prev.next = new_node


        

list1 = LinkedList()
list1.addBefore(1)
list1.addBefore(2)
list1.addBefore(3)
list1.printlist()
print("")
list1.append(4)
list1.insert(list1.head, 5)
list1.printlist()




