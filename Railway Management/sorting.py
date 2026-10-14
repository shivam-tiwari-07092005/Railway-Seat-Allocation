#bubble sort
def bubble_sort(unordered_list):
    itr = len(unordered_list)
    for i in range(itr):
        print(f"Iteration {i}: ")
        for j in range(0, itr - i - 1):
            if unordered_list[j] > unordered_list[j+1]:
                temp = unordered_list[j]
                unordered_list[j] = unordered_list[j+1]
                unordered_list[j+1] = temp
                print(unordered_list)
input_list = input("Enter number separated by spaces: ")
unordered_list = list(map(int, input_list.split()))
bubble_sort(unordered_list)
print(unordered_list)

#insertion sort
def insertion_sort(unsorted_list):
    for i in range(1, len(unsorted_list)):
        j = i
        insert_value = unsorted_list[i]
        while j > 0 and unsorted_list[j-1] > insert_value:
            unsorted_list[j] = unsorted_list[j-1]
            j -= 1
        unsorted_list[j] = insert_value
        print(f"Current list: {unsorted_list}")
try:
    user_input = input("Enter numbers separated by space: ")
    my_list = list(map(int, user_input.split()))
    print("Original list: ", my_list)
    insertion_sort(my_list)
    print("Sorted list: ", my_list)
except ValueError:
    print("Please enter a valid seqeunce of integers separated by spaces!")

#selection sort
def selection_sort(unsorted_list):
    size_of_list = len(unsorted_list)
    for i in range(size_of_list - 1):
        min_index = i
        for j in range(i + 1, size_of_list):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j
        if min_index != i:
            unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]
user_input = input("Enter numbers separated by spaces: ")
input_list = list(map(int, user_input.split()))
if not input_list:
    print("The list is empty!")
else:
    print(f"Original list: {input_list}")
    selection_sort(input_list)
    print(f"Sorted list: {input_list}")

#quick sort
def divide(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break
    arr[low], arr[right] = arr[right], arr[low]
    return right
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = divide(arr, low, high)
        quick_sort(arr, low, pivot_index-1)
        quick_sort(arr, pivot_index+1, high)
user_input = input("Enter the element of the array separated by space: ")
array = list(map(int, user_input.split()))
print("Original array: ", array)
quick_sort(array, 0, len(array)-1)
print("Sorted array: ", array)

#merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
user_input = input("Enter the element of the array separated by spaces: ")
arr = list(map(int, user_input.split()))
print("Orginal array: ", arr)
merge_sort(arr)
print("Sorted array: ", arr)

#radix sort
def get_max(arr):
    return max(arr)
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    i = n-1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index]-1] = arr[i]
        count[index] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]
def radix_sort(arr):
    max_num = get_max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
user_input = input("Enter the elements separated by space: ")
arr = list(map(int, user_input.split()))
print("Original list: ", arr)
radix_sort(arr)
print("Sorted array: ", arr)