#traverse SLL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head, tail = None, None
n = int(input("Enter number of nodes: "))
for i in range(n):
    data = int(input("Enter data: "))
    newNode = Node(data)
    if head is None:
        head = newNode
        tail = newNode
    else:
        tail.next = newNode
        tail = newNode
print("Element of LL: ")
temp = head
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next

#traverse CLL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head, tail = None, None
n = int(input("Enter number of nodes: "))
for i in range(n):
    data = int(input("Enter data: "))
    newNode = Node(data)
    if head is None:
        head = newNode
        tail = newNode
    else:
        tail.next = newNode
        tail = newNode
tail.next = head
print("Elements of CLL: ")
temp = head
while True:
    print(temp.data, end=" ")
    temp = temp.next
    if temp == head:
        break

#Traverse DLL
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
head, tail = None, None
n = int(input("Enter number of nodes: "))
for i in range(n):
    data = int(input("Enter data: "))
    newNode = Node(data)
    if head is None:
        head = newNode
        tail = newNode
    else:
        tail.next = newNode
        newNode.prev = tail
        tail = newNode
print("Elements from end to beginning: ")
temp = tail
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.prev