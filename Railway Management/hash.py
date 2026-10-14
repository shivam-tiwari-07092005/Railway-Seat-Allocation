#Separate
size = 10
table = [[] for i in range(size)]
n = int(input("Enter number of elements: "))
for i in range(n):
    key = int(input("Enter key: "))
    index = key % size
    table[index].append(key)
print("Separate chaining: ")
for i in range(size):
    print(i, ":", table[i])

#Quadratic
size = 10
table = [None] * size
n = int(input("Enter number of elements: "))
for i in range(n):
    key = int(input("Enter key: "))
    index = key % size
    j = 0
    while table[(index + j * j) % size] is not None:
        j += 1
    table[(index + j * j) % size] = key
print("Quadratic probing: ")
for i in range(size):
    print(i, ":", table[i])

#Linear
size = 10
table = [None] * size
n = int(input("Enter number of elements: "))
for i in range(n):
    key = int(input("Enter key: "))
    index = key % size
    while table[index] is not None:
        index = (index + 1) % size
    table[index] = key
print("Linear probing: ")
for i in range(size):
    print(i, ":", table[i])