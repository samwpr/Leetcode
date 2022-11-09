class Node:
    def __init__(self, input):
        self.root = input
        self.left = None 
        self.right = None 
    

    def add(self, input):
        if self.root:
            if input <= self.root:
                if self.left == None:
                    self.left = Node(input)
                else:
                    self.left.add(input)
            else: 
                if self.right == None:
                    self.right = Node(input)
                else:
                    self.right.add(input)
        else:
            self.root = input

    def inorder(self, tree):
        res = []
        if tree: 
            res = res + self.inorder(tree.left)
            res.append(tree.root)
            res = res + self.inorder(tree.right)
        return res 

tree1 = Node(5)
tree1.add(2)
tree1.add(7)

print(tree1.inorder(tree1))

