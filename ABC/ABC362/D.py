import heapq

def solve(N, M, A, edges):
    graph = [[] for _ in range(N)]
    for u, v, w in edges:
        graph[u - 1].append((v - 1, w))
        graph[v - 1].append((u - 1, w))

    dist = [float('inf')] * N
    dist[0] = A[0]

    queue = [(dist[0], 0)]
    while queue:
        d, u = heapq.heappop(queue)
        if dist[u] < d:
            continue
        for v, w in graph[u]:
            cost = d + w + A[v]
            if cost < dist[v]:
                dist[v] = cost
                heapq.heappush(queue, (cost, v))

    return dist[1:]

N, M = map(int, input().split())
A = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(M)]

ans = solve(N, M, A, edges)
print(*ans)
