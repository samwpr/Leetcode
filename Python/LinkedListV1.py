class Node: 
    def __init__(self, input):
        self.next = None
        self.data = input 

class LinkedList:
    def __init__(self):
        self.head = None

    def printRoot(self):
        print(self.head.data)

    def printList(self):
        temp = self.head 
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next 
        print("")

    def addBefore(self, input):
        new_node = Node(input)
        new_node.next = self.head
        self.head = new_node
    
    def append(self, input):
        new_node = Node(input)
        if self.head is None:
            self.head = new_node
            return 
        
        tail = self.head 
        while tail.next != None:
            tail = tail.next 
        tail.next = new_node
    
    def insert(self, prevNode, input):
        if prevNode is None:
            print("Previous node doesn't exist")
            return 
        
        new_node = Node(input)
        new_node.next = prevNode.next
        prevNode.next = new_node

    def merge(self, list1, list2):
        dummy = Node(0)
        tail = dummy

        while list1 and list2:
            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next 
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next

    def reverseIT(self):
        curr = self.head 
        prev, temp = None, None
        while curr is not None:
            prev = curr
            curr = curr.next 
            prev.next = temp
            temp = prev
        self.head = prev
        return prev
    
    def reverseRE(self, head):
        if not head:
            return None
        
        newhead = head
        if head.next:
            newhead = self.reverseRE(head.next)
            head.next.next = head
        head.next = None
        return newhead
        




    
list1 = LinkedList()
list1.addBefore(6)
list1.addBefore(4)
list1.addBefore(2)
list1.printRoot()
list1.printList()

list2 = LinkedList()
list2.append(1)
list2.append(3)
list2.append(7)
list2.insert(list2.head.next, 5)
list2.printList()

list1.head = list1.merge(list1.head, list2.head)
list1.printList()
list1.reverseIT()
list1.printList()
list1.head = list1.reverseRE(list1.head)
list1.printList()


