# #insertion using LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
front, rear = None, None
n = int(input("Enter number of elements: "))
for i in range(n):
    data = int(input("Enter element: "))
    new_node = Node(data)
    if front is None:
        front = new_node
        rear = new_node
    else:
        rear.next = new_node
        rear = new_node
print("Queue after insertion: ")
temp = front
while temp is not None:
    print(temp.data, end =" ")
    temp = temp.next

# #insertion and deletion using array
queue = []
size = int(input("Enter size of queue: "))
while True:
    print("Insert, delete, display, exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        if len(queue) == size:
            print("Queue is full")
        else:
            data = int(input("Enter the element: "))
            queue.append(data)
            print("Element inserted!")
    elif choice == 2:
        if len(queue) == 0:
            print("Queue is empty!")
        else:
            data = queue.pop(0)
            print("Deleted element: ", data)
    elif choice == 3:
        if len(queue) == 0:
            print("Queue is empty!")
        else:
            print("Deleted element: ", queue)
    elif choice == 4:
        print("Program ended")
        break
    else:
        print("Invalid choice!")
    