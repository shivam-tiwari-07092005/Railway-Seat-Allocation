#Linear
def linear_search(lst, key):
    for i in range(len(lst)):
        if key == lst[i]:
            print("Element found!")
            print(i+1, "is the position of element ", lst[i])
            break
        else:
            print("Element not found!")
lst = list(map(int, input("Enter the list numbers separated by spaces: ").split()))
key = int(input("Enter the key element: "))
linear_search(lst, key)

#Binary search
def binary_search(lst, key):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == key:
            return mid
        elif lst[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1
lst = list(map(int, input("Enter element of list in sorted order: ").split()))
key = int(input("Enter the key element: "))
result = binary_search(lst, key)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found!")