def find_fcfs_waiting_time(processes, n, burst_time, waiting_time):
    waiting_time[0] = 0
    for i in range(1, n):
        waiting_time[i] = burst_time[i-1] + waiting_time[i-1]

def find_fcfs_turnaround_time(processes, n, burst_time, waiting_time, turnaround_time):
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

def find_fcfs_average_time(processes, n, burst_time):
    waiting_time = [0] * n
    turnaround_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0
    find_waiting_time(processes, n, burst_time, waiting_time)
    find_turnaround_time(processes, n, burst_time, waiting_time, turnaround_time)
    print("PID    Burst time    Waiting time    Turnaround time")
    for i in range(n):
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]
        print(f"{processes[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    print(f"Average waiting time = {total_waiting_time / n:.5f}")
    print(f"Average turnaround time = {total_turnaround_time / n:.5f}")

def calculate_waiting_time(processes):
    processes[0]["waiting_time"] = 0
    for i in range(1, len(processes)):
        processes[i]["waiting_time"] = processes[i-1]["burst_time"] + processes[i-1]["waiting_time"]

def calculate_turnaround_time(processes):
    for process in processes:
        process["turnaround_time"] = process["burst_time"] + process["waiting_time"]

def priority_scheduling(processes):
    sorted_processes = sorted(processes, key = lambda x:x["priority"])
    total_waiting_time = 0
    total_turnaround_time = 0
    calculate_waiting_time(sorted_processes)
    calculate_turnaround_time(sorted_processes)
    print("PID    Priority    Burst time    Waiting time    Turnaround time")
    for process in sorted_processes:
        total_waiting_time += process["waiting_time"]
        total_turnaround_time += process["turnaround_time"]
        print(f"{process["pid"]}\t\t{process["priority"]}\t\t{process["burst_time"]}\t\t{process["waiting_time"]}\t\t{process["turnaround_time"]}")
    print(f"Average waiting time = {total_waiting_time / len(processes):.5f}")
    print(f"Average turnaround time = {total_turnaround_time / len(processes):.5f}")
    
class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

def round_robin(processes, time_quantum):
    time = 0
    while True:
        done = True
        for process in processes:
            if process.remaining_time > 0:
                done = False
                if process.remaining_time > time_quantum:
                    time += time_quantum
                    process.remaining_time -= time_quantum
                else:
                    time += process.remaining_time
                    process.turnaround_time = time + process.burst_time
                    process.remaining_time = 0
                    process.turnaround_time = process.waiting_time + process.burst_time
        if done:
            break

def print_processes(processes):
    print("PID       Burst time    Waiting time    Turnaround time")
    for process in processes:
        print(f" {process.pid}\t\t{process.burst_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")
