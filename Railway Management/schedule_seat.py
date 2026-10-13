def fcfs(requests, head):
    seek_sequence = []
    seek_count = 0
    current_head = head
    for request in requests:
        seek_sequence.append(request)
        seek_count += abs(current_head - request)
        current_head = request
    return seek_sequence, seek_count

def sstf(requests, head):
    requests = sorted(requests)
    seek_sequence = []
    seek_count = 0
    current_head = head
    while requests:
        distances = {req: abs(req - current_head) for req in requests}
        closest_request = min(distances, key = distances.get)
        seek_sequence.append(closest_request)
        seek_count += abs(current_head - closest_request)
        current_head = closest_request
        requests.remove(closest_request)
    return seek_sequence, seek_count

requests = [98, 183, 37, 122, 14, 124, 65, 67]
head = 53
sequence, count = fcfs(requests, head)
print(f"FCFS seek sequence: {sequence}")
print(f"Total seek count: {count}")
sequence, count = sstf(requests, head)
print(f"SSTF seek sequence: {sequence}")
print(f"Total seek count: {count}")