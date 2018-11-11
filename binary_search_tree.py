# binary_search_tree.py - practice python coding

class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


def Insert(node, key):
    if node == None:
        node = Node(key)
    else:
        if key < node.key:
            node.left = Insert(node.left, key)
        if key > node.key:
            node.right = Insert(node.right, key)
    return node


def Traverse(node):
    if (node.left == None and node.right == None):
        print(node.key)
        return
    if node.left != None:
        Traverse(node.left)
        print(node.key)
        if node.right != None:
            Traverse(node.right)
            return
    if node.right != None:
        print(node.key)
        Traverse(node.right)


# Test
node_list = [ 100, 50, 22, 75, 90, 85, 88, 95, 96, 97]
root = None
for key in node_list:
    node = Insert(root, key)
    if root == None:
        root = node

Traverse(root)

flag = True
while flag:
    key = int(input('Input node key: '))
    if key > 0:
        node = Insert(root, key)
        if root == None:
            root = node
    else:
        flag = 0

print('Traverse Tree')
Traverse(root)
