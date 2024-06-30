from collections import deque, defaultdict

def bfs(graph, start, A, target):
    """ Perform BFS to find the shortest path between start and any node with value target in A """
    queue = deque([(start, 0)])
    visited = set()
    while queue:
        node, dist = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        if A[node - 1] == target:
            return dist
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, dist + 1))
    return float('inf')

def solve(N, edges, A):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    total_sum = 0
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            if A[i - 1] == A[j - 1]:
                total_sum += bfs(graph, i, A, A[j - 1])
    
    return total_sum

# Read input
N = int(input())
edges = [tuple(map(int, input().split())) for _ in range(N-1)]
A = list(map(int, input().split()))

# Solve and print the result
print(solve(N, edges, A))
