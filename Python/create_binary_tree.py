class Node: 
    def __init__(self, input):
        self.left = None 
        self.right = None 
        self.data = input 

    def print_root(self): #After adding nodes what will this print?
        print(self.data)

    def add(self, input):
        if self.data: 
            if input < self.data:
                if self.left is None:
                    self.left = Node(input)
                else: 
                    self.left.add(input)

            if input > self.data:
                if self.right is None: 
                    self.right = Node(input)
                else: 
                    self.right.add(input)
        
        else:
            self.data = input

    def print_tree(self): #Inorder Traversal. Left -> Root -> Right or Smallest to Biggest 
        if self.left: 
            self.left.print_tree()
        print(self.data, end=" ")

        if self.right:
            self.right.print_tree()

    def in_order_traversal(self, binary_tree): #Inorder Traversal. Left -> Root -> Right. Smallest to Biggest 
        res = []
        if binary_tree:
            res = self.in_order_traversal(binary_tree.left)
            res.append(binary_tree.data)
            res = res + self.in_order_traversal(binary_tree.right)
        return res

    def pre_order_traversal(self, binary_tree): #Pre order Traversal. Root -> Left -> Right. 
        res = []
        if binary_tree:
            res.append(binary_tree.data)
            res = res + self.pre_order_traversal(binary_tree.left)
            res = res + self.pre_order_traversal(binary_tree.right)
        return res

    def post_order_traversal(self, binary_tree): #Left -> Right -> Root. 
        res =[]
        if binary_tree:
            res = res + self.post_order_traversal(binary_tree.left)
            res = res + self.post_order_traversal(binary_tree.right)
            res.append(binary_tree.data)
        return res

    
    def reverse(self, binary_tree):
        if not binary_tree: 
            return None 
        
        temp = binary_tree.left
        binary_tree.left = binary_tree.right
        binary_tree.right = temp  

        self.reverse(binary_tree.left)
        self.reverse(binary_tree.right)
        return root




root = Node(27)
root.add(14)
root.add(35)
root.add(10)
root.add(19)
root.add(31)
root.add(42)
root.print_tree()
print("")
print("In Order",root.in_order_traversal(root))
print("Pre Order",root.pre_order_traversal(root))
print("Post Order",root.post_order_traversal(root))
print("\n")
root.reverse(root)
root.print_tree()