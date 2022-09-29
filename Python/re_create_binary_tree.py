class Node:
    def __init__(self, input):
        self.left = None
        self.right = None 
        self.data = input 

    def printRoot(self):
        print(self.data)

    def add(self, input):
        if self.data != None: 
            if input < self.data:
                if self.left is None:
                    self.left = Node(input)
                else: 
                    self.left.add(input)
            else: 
                if self.right is None:
                    self.right = Node(input)
                else: 
                    self.right.add(input)
        else:
            self.data = input

    
    def in_order_traversal(self, root):
        res = []
        if root != None:
            res += self.in_order_traversal(root.left)
            res.append(root.data)
            res += self.in_order_traversal(root.right)
        return res

    def post_order_traversal(self, root):
        res = []
        if root != None: 
            res = self.post_order_traversal(root.left)
            res += self.post_order_traversal(root.right)
            res.append(root.data)
        return res 



root = Node(1)
root.add(2)
root.add(3)
root.add(4)
root.add(5)
#root.add(6)
#root.add(9)
print("In Order",root.in_order_traversal(root))
print("Post Order",root.post_order_traversal(root))

