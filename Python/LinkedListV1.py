class Node:
    def __init__(self, input: int, node = None):
        self.data = input 
        self.next_node = node

class LinkedList:
    def __init__(self, root_node = None): #Is there a need for root_node to be a parameter? 
        self.root = root_node
        self.size = 0 

    def add(self, input: int):
        new_node = Node(input, self.root)
        self.root = new_node
        self.size += 1

    def print(self):
        temp = self.root
        while temp != None: 
            print(temp.data, " ")
            temp = temp.next_node


myList = LinkedList()
myList.add(1)
myList.add(2)
myList.add(3)
myList.print()

#What is end=" "




