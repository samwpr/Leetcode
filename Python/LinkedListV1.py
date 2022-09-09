class Node(object):
    def __init__(self, data, node = None):
        self.data = data
        self.next_node = node

class LinkedList(object):
    def __init__(self):
        self.root = None

    def add(self, input):
        pass