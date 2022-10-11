'''
Link: https://leetcode.com/problems/reverse-linked-list/
Level: Easy
Companies: Inuit, Yandex
'''
class Node:
    def __init__(self, input):
        self.data = input 
        self.next = None 
    

class LinkedList:
    def __init__(self):
        self.head = None 

    def printHead(self):
        print(self.head.data)
    
    def printList(self):
        temp = self.head
        while temp != None: 
            print(temp.data, end=" ")
            temp = temp.next 
        print("")

    def addBefore(self, input): #O(n)
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
        if not prevNode:
            print("There is no prevous Node")
            return

        new_node = Node(input)
        new_node.next = prevNode.next
        prevNode.next = new_node

    def reverseIterative(self):
        curr = self.head
        temp = None

        while curr != None:
            prev = curr
            curr = curr.next
            prev.next = temp
            temp = prev 
        self.head = prev
        return prev
    
    def reverseRecursive(self, head):
        if not head:
            return None
        
        newhead = head
        if head.next:
            newhead = self.reverseRecursive(head.next)
            head.next.next = head 
        head.next = None 
        return newhead

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

    def hasCycle(self, head):
        slow, fast = head, head 

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast:
                return True
        return False


        

list1 = LinkedList()
list1.addBefore(1)
list1.addBefore(2)
list1.addBefore(3)
list1.printList()
list1.reverseIterative()
list1.printList()

list2 = LinkedList()
list2.append(1)
list2.append(2)
list2.append(4)
list2.insert(list2.head.next, 3)
list2.printList()

#list1.head = list1.merge(list1.head, list2.head)
#list1.printList()

list2.printList()
print(list2.hasCycle(list2.head))

print(list2.head.next.next.next.data)
list2.head.next.next.next = list2.head
print(list2.head.next.next.next.data)

print(list2.hasCycle(list2.head))

list2.printHead()
            
        




