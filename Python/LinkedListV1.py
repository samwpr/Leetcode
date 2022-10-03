from xml.etree.ElementPath import prepare_child


class Node:
    def __init__(self, input):
        self.data = input 
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None 

    def print(self):
        temp = self.head
        while temp != None: 
            print(temp.data, end=" ")
            temp = temp.next 
        print("")

    def addBefore(self, input): #O(1) constant time 
        new_node = Node(input)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prevNode, input): #O(1) constant time
        if prevNode == None: 
            print("Previous node not found")
            return 

        new_node = Node(input)
        new_node.next = prevNode.next 
        prevNode.next = new_node

    def append(self, input): #   O(n) number of nodes 
        new_node = Node(input)
        if self.head == None:
            self.head = new_node
            return 

        dummy = self.head 
        while dummy.next != None: 
            dummy = dummy.next

        dummy.next = new_node

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


def hasCycle(self, head): 
    slow = head
    fast = head

    while fast and fast.next: 
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True 
    return False

def merge(list1, list2): 
    dummyNode = Node(0)
    tail = dummyNode

    while True:
        if list1 is None: 
            tail.next = list2
            break
        if list2 is None: 
            tail.next = list1
            break 

        if list1.data <= list2.data: 
            tail.next = list1
            list1 = list1.next
        else: 
            tail.next = list2
            list2 = list2.next
        
        tail = tail.next 
    return dummyNode.next 


list1 = LinkedList()
list2 = LinkedList()

list1.addBefore(1)
list1.addBefore(5)
list1.print()

list1.insertAfter(list1.head, 3)
list1.print()
list1.reverse()
list1.print()

list2.append(2)
list2.append(4)
list2.append(6)
list2.print()

list1.head = merge(list1.head, list2.head)
list1.print()

list1.head.next.next.next = list1.head 

list1.head = hasCycle(list1.head)

print(list1.head)
