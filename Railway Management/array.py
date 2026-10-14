# # traverse and print element b/w ub and lb
n = int(input("Enter number of elements: "))
s = []
print("Enter the elements: ")
for _ in range(n):
    s.append(int(input()))
lb = int(input("Enter lower bound (0-based index): "))
ub = int(input("Enter upper bound (0-based index): "))
if lb < 0 or ub >= n or lb > ub:
    print("Invalid bounds!")
else:
    print("Traversed elements: ")
    l = lb
    while l <= ub:
        print(s[l])
        l += 1

# #sum of elements b/w lb and ub
n = int(input("Enter number of elements: "))
s = []
print("Enter the elements: ")
for _ in range(n):
    s.append(int(input()))
lb = int(input("Enter lower bound (0-based index): "))
ub = int(input("Enter upper bound (0-based index): "))
if lb < 0 or ub >= n or lb > ub:
    print("Invalid bounds!")
else:
    l = lb
    total = 0
    while l <= ub:
        total += s[l]
        l += 1
print(f"Sum of elements from index {lb} to {ub} is: {total}")

#insert at the k-th position
n = int(input("Enter number of elements: "))
s = []
print("Enter the elements: ")
for _ in range(n):
    s.append(int(input()))
k = int(input("Enter the position to insert new element (1-based index): "))
new_value = int(input("Enter the new element: "))
if k < 1 or k > n+1:
    print("Invalid position!")
else:
    k -= 1
    s.append(0)
    i = n - 1
    while i >= k:
        s[i + 1] = s[i]
        i -= 1
    s[k] = new_value
    n += 1
    print("Array after insertion: ")
    print(s)

# delete k-th position
n = int(input("Enter number of elements: "))
s = []
print("Enter the elements: ")
for _ in range(n):
    s.append(int(input()))
k = int(input("Enter the position to delete the element (1-based index): "))
if k <= 0 or k > n:
    print("Invalid position!")
else:
    s.pop(k - 1)
    print(s)

# add 2 arrays and print it sorted
n1 = int(input("Enter number of elements: "))
a1 = []
print("Enter the elements: ")
for _ in range(n1):
    a1.append(int(input()))
n2 = int(input("Enter number of elements: "))
a2 = []
print("Enter the elements: ")
a = []
for _ in range(n1):
    a2.append(int(input()))
for i in range(n1):
    a.append(a1[i])
for j in range(n2):
    a.append(a2[j])
n = n1 + n2
i = 0
while i < n-1:
    j = 0
    while j < n-i-1:
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j+1] = temp
        j += 1
    i += 1
print(f"Sorted array: {a}")

#matrix add, mul and transpose
r1 = int(input("Enter number of rows (1st matrix): "))
c1 = int(input("Enter number of columns (1st matrix): "))
M1 = []
print("Enter elements of 1st matrix row by row:")
for i in range(r1):
    row = []
    for j in range(c1):
        row.append(int(input()))
    M1.append(row)
r2 = int(input("Enter number of rows (2nd matrix): "))
c2 = int(input("Enter number of columns (2nd matrix): "))
M2 = []
print("Enter elements of 2nd matrix row by row:")
for i in range(r2):
    row = []
    for j in range(c2):
        row.append(int(input()))
    M2.append(row)
if r1 == r2 and c1 == c2:
    add = []
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(M1[i][j] + M2[i][j])
        add.append(row)
    print("Matrix addition: ")
    for row in add:
        print(row)
else:
    print("Addition not possible!")
if c1 == r2:
    mul = []
    for i in range(r1):
        row = []
        for j in range(c2):
            total = 0
            for k in range(c1):
                total += M1[i][k] * M2[k][j]
            row.append(total)
        mul.append(row)
    print("Matrix multiplication: ")
    for row in mul:
        print(row)
else:
    print("Multiplication not possible!")
transpose1 = []
for i in range(c1):
    row = []
    for j in range(r1):
        row.append(M1[j][i])
    transpose1.append(row)
print("Transpose of 1st matrix: ")
for row in transpose1:
    print(row)
transpose2 = []
for i in range(c2):
    row = []
    for j in range(r2):
        row.append(M2[j][i])
    transpose2.append(row)
print("Transpose of 2nd matrix: ")
for row in transpose2:
    print(row)
