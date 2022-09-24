'''
Link: https://leetcode.com/problems/merge-two-sorted-lists/
Level: Easy
Companies: Accenture, Adobe, Orcale, Shoppe
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, root = None):
        self.root = root
        self.size = 0

    def add(self, val):
        new_node = ListNode(val, self.root)
        self.root = new_node
        self.size += 1

    def print(self): 
        list = []
        temp = self.root
        while temp != None: 
            list.append(temp.val)
            temp = temp.next
        return list


    def mergeTwoLists(self, list1, list2):
        dummyNode = ListNode(0)
        tail = dummyNode
        while True:
            if list1 is None:
                tail.next = list2
                break
            if list2 is None: 
                tail.next = list1
                break

            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else: 
                tail.next = list2
                list2 = list2.next

            tail = tail.next 
        return dummyNode.next




list1 = LinkedList()
list1.add(4)
list1.add(2)
list1.add(1)
print("List 1", list1.print())

list2 = LinkedList()
list2.add(4)
list2.add(3)
list2.add(1)
print("List 2", list2.print())

list3 = []

list1.mergeTwoLists(list1.root, list2.root).print()



'''
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
'''