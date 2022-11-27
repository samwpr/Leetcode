
class Node:
    def __init__(self, input):
        self.root = input
        self.left = None
        self.right = None

    def add(self, input):
        if self.root:
            if input < self.root:
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

    def inOrder(self, tree):
        res = []
        if tree:
            res = res + self.inOrder(tree.left)
            res.append(tree.root)
            res = res + self.inOrder(tree.right)

        return res


root = Node(4)
root.add(2)
root.add(7)
root.add(1)
root.add(3)
root.add(6)
root.add(9)
#root.print_root()
#root.print_tree()

print("")
print("In Order",root.inOrder(root))
#print("Pre Order",root.pre_order_traversal(root))
#print("Post Order",root.post_order_traversal(root))
#print("\n")
#root.reverse(root)
#root.print_tree()
#root.printLevelOrder(root)
#root.reverse(x)
#root.print_tree()
#print("\n")

#root.printLevelOrder2(root)