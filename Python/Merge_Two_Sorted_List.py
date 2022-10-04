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
            print("Previous node not found")
            return 
        
        new_node = Node(input)
        new_node.next = prevNode.next
        prevNode.next = new_node

    def reverse(self):
        curr = self.head
        temp = None 
        while curr != None: 
            prev = curr
            curr = curr.next 
            prev.next = temp 
            temp = prev
        self.head = prev 
        return prev 

    def hasCycle(self, head):
        slow, fast = head, head 

        while fast.next != None:
            slow = slow.next 
            fast = fast.next.next
            if fast == slow:
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
list1.append(2)
list1.append(4)
list1.append(6)
list1.print()


list2 = LinkedList()
list2.append(1)
list2.append(2)
list2.append(3)
list2.print()

#Creating a cycle 
print(list1.head.next.next.next)
list1.head.next.next.next = list1.head 
print(list1.head.next.next.next.data)
print(list1.hasCycle(list1.head))
print(list2.hasCycle(list2.head))
