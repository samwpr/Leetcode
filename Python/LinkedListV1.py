class Node(object):
    def __init__(self, input: int, node = None):
        self.data = input
        self.next_node = node

class LinkedList(object):
    def __init__(self, rootNode = None):
        self.root = rootNode
        self.size = 0
    
    def add(self, input: int):
        NEW_node = Node(input, self.root)
        self.root = NEW_node
        self.size += 1

    def printList(self):
        temp = self.root
        while temp != None:
            print(temp.data)
            temp = temp.next_node
        print("")

myList = LinkedList()
myList.add(5)
myList.add(8)
myList.printList() 
#8
#5
