#Make append O(1)
#https://www.youtube.com/watch?v=l92wSWAZmnI&ab_channel=SaiAnishMalla


from multiprocessing import dummy

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
            print(temp.data, end="")
            temp = temp.next
        print("")

    def addFront(self, input): #O(1) constant about of work 
        new_node = Node(input)
        new_node.next = self.head
        self.head = new_node
   
    def append(self, input): #O(n) where n is number of nodes in the linkedlist.
        new_node = Node(input)
        if self.head == None:
            self.head = new_node
            return 
        
        tail = self.head
        while tail.next != None:
            tail = tail.next 

        tail.next = new_node

    def insertAfter(self, prev_node, input): #O(1) constant amount of work 
        if prev_node is None: 
            print("This is no previous node")
            return 
        
        new_node = Node(input)
        new_node.next = prev_node.next
        prev_node.next = new_node

def mergeList(headA, headB):
    dummyNode = Node(0)
    tail = dummyNode
    while True: 
        if headA is None:
            tail.next = headB
            break
        if headB is None:
            tail.next = headA
            break

        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next
        tail = tail.next
    return dummyNode.next
        

list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.print()

list2 = LinkedList()
list2.addFront(1)
list2.addFront(2)
list2.addFront(3)
list2.print()
list2.insertAfter(list2.head.next, 4)
list2.print()

list1.head = mergeList(list1.head, list2.head)
list1.print()
print("------------")
