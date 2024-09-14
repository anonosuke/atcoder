import itertools

N = int(input())
M_G = int(input())
edges_G = [tuple(map(int, input().split())) for _ in range(M_G)]

M_H = int(input())
edges_H = [tuple(map(int, input().split())) for _ in range(M_H)]

adj_G = [[0]*N for _ in range(N)]
adj_H = [[0]*N for _ in range(N)]

for u, v in edges_G:
    adj_G[u-1][v-1] = 1
    adj_G[v-1][u-1] = 1

for u, v in edges_H:
    adj_H[u-1][v-1] = 1
    adj_H[v-1][u-1] = 1

A_list = []
total_costs = N * (N - 1) // 2
while len(A_list) < total_costs:
    line = input().strip()
    if line:
        A_list.extend(map(int, line.split()))

A = [[0]*N for _ in range(N)]
index = 0
for i in range(N-1):
    for j in range(i+1, N):
        cost = A_list[index]
        index += 1
        A[i][j] = cost
        A[j][i] = cost

min_cost = float('inf')
for perm in itertools.permutations(range(N)):
    cost = 0
    for i in range(N):
        for j in range(i+1, N):
            u = perm[i]
            v = perm[j]
            edge_G = adj_G[u][v]
            edge_H = adj_H[i][j]
            if edge_G != edge_H:
                cost += A[i][j]
    if cost < min_cost:
        min_cost = cost

print(min_cost)
