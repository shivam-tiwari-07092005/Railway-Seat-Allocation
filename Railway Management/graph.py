#BFS
from collections import deque
n = int(input("Enter number of vertices: "))
adj = [[] for _ in range(n)]
e = int(input("Enter number of edges: "))
print(f"Enter {e} edges. Vertices should be between 0 and {n-1} (separated by a space):")
for i in range(e):
    u, v = map(int, input(f"Edge {i+1}: ").split())
    adj[u].append(v)
    adj[v].append(u)
start = int(input("Enter starting vertex: "))
visited = [False] * n
q = deque([start])
visited[start] = True
print("BFS Traversal: ", end="")
while q:
    node = q.popleft()
    print(node, end=" ")
    for neigh in adj[node]:
        if not visited[neigh]:
            visited[neigh] = True
            q.append(neigh)

#DFS
n = int(input("Enter number of vertices: "))
adj = [[] for _ in range(n)]
e = int(input("Enter number of edges: "))
for i in range(e):
    u, v = map(int, input(f"Edge {i+1}: ").split())
    adj[u].append(v)
    adj[v].append(u)
start = int(input("Enter starting vertex: "))
visited = [False] * n
def dfs(node):
    visited[node] = True
    print(node, end="")
    for neigh in adj[node]:
        if not visited[neigh]:
            dfs(neigh)
print("DFS traversal: ", end=" ")
dfs(start)