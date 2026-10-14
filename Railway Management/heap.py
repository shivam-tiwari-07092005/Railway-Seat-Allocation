#MAX heap
def heapify_up(heap, i):
    while i > 0:
        parent = (i-1) // 2
        if heap[i] > heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break
heap = []
n = int(input("Enter the number of elements: "))
for _ in range(n):
    x = int(input("Enter value: "))
    heap.append(x)
    heapify_up(heap, len(heap)-1)
print("MAX heap: ", heap)

#MIN heap
def heapify_up(heap, i):
    while i > 0:
        parent = (i-1) // 2
        if heap[i] < heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break
heap = []
n = int(input("Enter the number of elements: "))
for _ in range(n):
    x = int(input("Enter value: "))
    heap.append(x)
    heapify_up(heap, len(heap)-1)
print("MIN heap: ", heap)