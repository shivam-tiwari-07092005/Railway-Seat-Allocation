#BT and print element
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
root = None
n = int(input("Enter the number of elements: "))
print("Enter the elements: ")
elements = []
for i in range(n):
    element = int(input())
    elements.append(element)
for e in elements:
    root = insert(root, e)
print("Element of binary tree: ", elements)
print("Inorder traversal: ")
inorder(root)
print("\nPreorder traversal: ")
preorder(root)
print("\nPostorder traversal: ")
postorder(root)

#In traverse
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def build_tree(position="root"):
    user_input = input(f"Enter element for {position} (or press Enter to skip): ").strip()
    if not user_input:
        return None
    root = Node(int(user_input))
    root.left = build_tree(f"left child of {root.data}")
    root.right = build_tree(f"right child of {root.data}")
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
root = build_tree()
print("Inorder traversal: ")
inorder(root)
print("\nPreorder traversal: ")
preorder(root)
print("\nPostorder tarversal: ")
postorder(root)
print()