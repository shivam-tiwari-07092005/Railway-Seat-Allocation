def is_safe(processes, available, max_need, allocation):
    n = len(processes)
    m = len(available)
    need = [[max_need[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]
    finish = [False] * n
    safe_sequence = []
    work = available[:]
    while len(safe_sequence) < n:
        found = False
        for i in range(n):
            if not finish[i]:
                if all (need[i][j] <= work[j] for j in range(m)):
                    for j in range(m):
                        work[j] += allocation[i][j]
                    safe_sequence.append(processes[i])
                    finish[i] = True
                    found = True
        if not found:
            print("System is not in a safe state!")
            return False, []
    print("System is in a safe state!")
    print("Safe sequence is: ", safe_sequence)
    return True, safe_sequence