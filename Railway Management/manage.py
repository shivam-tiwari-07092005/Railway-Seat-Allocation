def first_fit(block_sizes, process_sizes):
    allocation = [-1] * len(process_sizes)
    for i in range(len(process_sizes)):
        for j in range(len(block_sizes)):
            if block_sizes[j] >= process_sizes[i]:
                allocation[i] = j
                block_sizes[j] = process_sizes[i]
                break
    print("First fit allocation: ")
    print_allocation(allocation, process_sizes)

def best_fit(block_sizes, process_sizes):
    allocation = [-1] * len(process_sizes)
    for i in range(len(process_sizes)):
        best_index = -1
        for j in range(len(block_sizes)):
            if block_sizes[j] >= process_sizes[i]:
                if best_index == -1 or block_sizes[j] < block_sizes[best_index]:
                    best_index = j
        if best_index != -1:
            allocation[i] = best_index
            block_sizes[best_index] -= process_sizes[i]
    print("Best fit allocation: ")
    print_allocation(allocation, process_sizes)

def worst_fit(block_sizes, process_sizes):
    allocation = [-1] * len(process_sizes)
    for i in range(len(process_sizes)):
        worst_index = -1
        for j in range(len(block_sizes)):
            if block_sizes[j] >= process_sizes[i]:
                if worst_index == -1 or block_sizes[j] > block_sizes[worst_index]:
                    worst_index = j
        if worst_index != -1:
            allocation[i] = worst_index
            block_sizes[worst_index] -= process_sizes[i]
    print("Worst fit allocation: ")
    print_allocation(allocation, process_sizes)

def print_allocation(allocation, process_sizes):
    print("PID    Process size    Block number")
    for i in range(len(process_sizes)):
        print(f"{i+1}\t\t{process_sizes[i]}\t\t", end = "")
        if allocation[i] != -1:
            print(f"{allocation[i] + 1}")
        else:
            print("Not allocated!")

block_sizes = [100, 500, 200, 300, 600]
process_sizes = [212, 417, 112, 426]
first_fit(block_sizes.copy(), process_sizes)
best_fit(block_sizes.copy(), process_sizes)
worst_fit(block_sizes.copy(), process_sizes)